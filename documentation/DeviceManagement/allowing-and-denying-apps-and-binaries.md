# Allowing and denying apps and binaries

**Framework**: Device Management

Control what apps and binaries can run on supervised Apple devices.

#### Overview

On supervised devices running iOS 27, iPadOS 27, macOS 27, tvOS 27, or visionOS 27, you can manage the apps people can run by using the [`AppSettings`](appsettings.md) configuration. This configuration offers two pairs of keys for granular, flexible control of what apps and binaries can run, as detailed in the table below.

| Key | Platform | System scope | User scope |
| --- | --- | --- | --- |
| `AllowedApps`, `DeniedApps` | iOS, iPadOS, tvOS, visionOS | Supported | Shared iPad only |
| `AllowedBinaries`, `DeniedBinaries` | macOS | Supported | — |

The configuration offers two primary modes on supported platforms:

- **Deny mode**: Configure `DeniedApps` or `DeniedBinaries`. The device prevents specified apps and binaries from launching and quits them if they’re already running. It allows all other apps and binaries to run.
- **Allow mode**: Configure `AllowedApps` or `AllowedBinaries`. The device allows only specified apps and binaries to run, along with essential apps and binaries included in the operating system. It prevents any other apps and binaries from launching and quits them if they’re already running.

Both modes use an array of apps and binaries that specify which items the device allows or denies. You can apply multiple configurations to a device, as detailed in the table below.

| Key for iOS, iPadOS, tvOS, and visionOS | Key for macOS | Combine type | Result |
| --- | --- | --- | --- |
| `AllowedApps` | `AllowedBinaries` | `set-intersection` | The device allows only entries listed in the configuration to run. If you apply multiple configurations, an app or binary needs to appear in all of them for the device to allow it. |
| `DeniedApps` | `DeniedBinaries` | `set-union` | The device prevents entries listed in each configuration from running. |

If you apply both an allow and a deny key, the device uses the more restrictive mode and denies apps and binaries unless the configuration explicitly allows them.

If an app or binary appears in both lists, the device prevents it from running.

#### Allow and Deny Binaries in Macos

In macOS, the configuration uses an Endpoint Security client and can manage standalone binaries and binaries embedded in an app bundle. You can create rules for the policy the Endpoint Security client uses to decide whether to allow or deny a binary.

For more information on the architecture and decision process, see [`Allow and deny apps and binaries`](https://developer.apple.comhttps://support.apple.com/guide/deployment/dep001044b08).

#### Create Binary Matching Rules

For the Endpoint Security client to allow or deny a binary, provide the necessary identifiers in the configuration.

The Endpoint Security client uses the following code signature attributes for binary matching:

- **`CDHash`**: The code signature code directory hash of the specific binary slice to match. A binary can contain multiple slices to support different hardware architectures, for example, universal binaries.
- **`PathPrefix`**: The file system path prefix to match binaries.
- **`SigningID`**: The code signature signing identifier of the binary.
- **`SigningState`**: The code signing state to match binaries. If there’s no state specified, the rule uses `All` by default.
- **`TeamID`**: The code signature team identifier of the binary. Use the value `*APPLE*` instead of an empty string for Apple binaries with an empty team identifier.

`SigningState` can be one of the following values:

- **`All`**: Matches binaries in any of the states of this table. Unsigned, ad hoc–signed, and development-signed binaries aren’t matched.
- **`TestFlight`**: Apps distributed using TestFlight.
- **`DeveloperID`**: Binaries signed with an Apple Developer account.
- **`Enterprise`**: Binaries signed with an in-house distribution provisioning profile.
- **`AppStore`**: Apps distributed using the App Store.
- **`Apple`**: Binaries signed by Apple.

You can retrieve the attributes using the `codesign` command. Because binaries can contain individual slices with separate execution paths for different architectures, first run `lipo -archs` to get a list of architectures. Use the returned value for the `--arch` parameter of the `codesign` command.

To cover multiple architectures, include separate rules for each possible slice in the configuration.

> **Note**:  The Mac App Store uses app thinning and provides only the slice relevant for the device that downloads the app.

This code block shows an example and highlights the returned values:

```sh
% lipo -archs /System/Applications/Chess.app/Contents/MacOS/Chess
arm64e

% codesign -dvvv --arch arm64e /System/Applications/Chess.app 
Executable=/System/Applications/Chess.app/Contents/MacOS/Chess # PathPrefix — for example, /System/Applications
Identifier=com.apple.Chess # SigningID
Format=app bundle with Mach-O thin (arm64e)
CodeDirectory v=20400 size=1512 flags=0x0(none) hashes=37+7 location=embedded
Platform identifier=26
Hash type=sha256 size=32
CandidateCDHash sha256=b7ec1f46a29e16837299bf9e6d8d8ca6c7ed2bb1
CandidateCDHashFull sha256=b7ec1f46a29e16837299bf9e6d8d8ca6c7ed2bb1cf4004a8ffce607a4f421398
Hash choices=sha256
CMSDigest=b7ec1f46a29e16837299bf9e6d8d8ca6c7ed2bb1cf4004a8ffce607a4f421398
CMSDigestType=2
CDHash=b7ec1f46a29e16837299bf9e6d8d8ca6c7ed2bb1 # CDHash
Signature size=4567
Authority=macOS Software Signing # SigningState
Authority=Apple Code Signing Certification Authority
Authority=Apple Root CA
Signed Time=25. Jun 2026 at 12:26:52
Info.plist entries=35
TeamIdentifier=not set # TeamID
Sealed Resources version=2 rules=2 files=0
Internal requirements count=1 size=64
Total signatures=1
Chosen signature=1
```

The first `Authority` value that `codesign` returns indicates the code signing state, as detailed in the table below.

| `Authority` value | `SigningState` |
| --- | --- |
| `macOS Software Signing` | `Apple` |
| `Apple Mac OS Application Signing` | `AppStore` |
| `Developer ID Application` | Check the OID using the following method. |
| `Apple Distribution` | Check the OID using the following method. |

Inspect the signing authority chain to further distinguish the code signing state of a binary, like this:

```sh
codesign -d --extract-certificates=/tmp/c /Applications/Example.app 2>/dev/null && \
  openssl x509 -inform DER -in /tmp/c0 -noout -text | \
  grep -oE '1\.2\.840\.113635\.100\.6\.1\.[0-9.]+'
```

The command returns one or more OIDs. If the returned list contains `1.2.840.113635.100.6.1.25.1` among other entries, the `SigningState` is `TestFlight`. Map the returned OIDs to the `SigningState` value using the following table.

| `OID` | `SigningState` |
| --- | --- |
| `1.2.840.113635.100.6.1.9` | `AppStore` |
| `1.2.840.113635.100.6.1.13` | `DeveloperID` |
| `1.2.840.113635.100.6.1.25.1` | `TestFlight` |
| `1.2.840.113635.100.6.1.4` | `Enterprise` |

For platform binaries, use the `Authority` value to determine the `SigningState`. Platform binaries don’t have an OID, so their `SigningState` is `Apple`.

If `codesign` returns an ad hoc `Signature` value, or if the certificate contains OID `1.2.840.113635.100.6.1.12` to indicate a development signature, the device denies the binary.

#### Deny Specific Binaries

When the Endpoint Security client denies a binary, it shows an alert to inform the user that their organization prevented the use of the binary.

Use one of the following required attributes to create a `DeniedBinaries` list entry:

- `CDHash`
- `SigningID`
- `TeamID`

You can optionally specify:

- `PathPrefix`
- `SigningState`

You can combine multiple required and optional values — up to all five identifiers — to form more specific rules.

The value of `CDHash` relates to the content of a specific binary and usually differs between versions. For example, use `CDHash` to deny a specific version of a binary that otherwise shares the same `TeamID` and `SigningID` as other versions.

To deny Web Clips, use the following entry in `DeniedBinaries`:

```json
"DeniedBinaries": [
    {
        "SigningID": "com.apple.Safari.WebApp"
    }
]
```

#### Allow Only Specific Binaries

Use one of the following required attributes to create an  `AllowedBinaries` list entry:

- `CDHash`
- `TeamID`

You can optionally specify:

- `PathPrefix`
- `SigningID`
- `SigningState`

Because `SigningID` isn’t globally unique across teams, `AllowedBinaries` requires a verifiable attribute such as `CDHash` or `TeamID`.

You can combine multiple required and optional values — up to all five identifiers — to form more specific rules.

The [`AppSettings`](appsettings.md) configuration has an `AlwaysAllowManagedApps` key to simplify managing allow lists. You deploy managed apps with the [`AppManaged`](appmanaged.md) configuration or set the `InstallAsManaged` flag to `true` in the [`InstallApplicationCommand`](installapplicationcommand.md). Set the `AlwaysAllowManagedApps` key to `true` to automatically allow managed apps to run in allow mode.

Even when you set this key, you can still deny individual managed apps using the `DeniedBinaries` key.

> **Note**:  Applying a configuration that only contains the `AlwaysAllowManagedApps` key doesn’t change the policy. Combine it with the `AllowedBinaries` key to allow only managed apps to run.

To allow Web Clips, use the following entry in `AllowedBinaries`:

```json
"AllowedBinaries": [
    {
        "TeamID": "*APPLE*",
        "SigningID": "com.apple.Safari.WebApp"
    }
]
```

#### Configure Allow and Deny Scenarios

The following examples show `AllowedBinaries` and `DeniedBinaries` combinations in macOS.

Allow all apps and binaries, but deny a specific one, as follows:

```json
{
    "Type": "com.apple.configuration.app.settings",
    "Identifier": "AF389B6F-5784-4DB6-BEFF-EA6D689BD4B0",
    "ServerToken": "A5CA3371-559E-44B4-B9ED-A0A7DFEC193A",
    "Payload": {
        "Allowed": {
            "DeniedBinaries": [
                {
                    "SigningID": "com.apple.MobileSMS"
                }
            ]
        }
    }
}
```

Allow all apps and binaries, but deny a specific version of one binary, as follows:

```json
{
    "Type": "com.apple.configuration.app.settings",
    "Identifier": "E2AA937B-12FB-44D4-88C0-FC109AABC395",
    "ServerToken": "A5CA3371-559E-44B4-B9ED-A0A7DFEC193A",
    "Payload": {
        "Allowed": {
            "DeniedBinaries": [
                {
                    "CDHash": "b7ec1f46a29e16837299bf9e6d8d8ca6c7ed2bb1"
                }
            ]
        }
    }
}
```

Deny all apps and binaries, but allow a specific one and apps provided by Apple, as follows:

```json
{
    "Type": "com.apple.configuration.app.settings",
    "Identifier": "FCC3B88C-C44A-4365-8D0B-57F17098CB74",
    "ServerToken": "A5CA3371-559E-44B4-B9ED-A0A7DFEC193A",
    "Payload": {
        "Allowed": {
            "AllowedBinaries": [
                {
                    "TeamID": "XXXXXXXXXX",
                    "SigningID": "com.example.app"
                },
                {
                    "TeamID": "*APPLE*"
                }
            ]
        }
    }
}
```

Deny all apps and binaries, but allow a specific one and apps provided by Apple, except Messages, as follows:

```json
{
    "Type": "com.apple.configuration.app.settings",
    "Identifier": "B94249B4-C9A1-446E-AFF7-F7C05AF730D6",
    "ServerToken": "A5CA3371-559E-44B4-B9ED-A0A7DFEC193A",
    "Payload": {
        "Allowed": {
            "AllowedBinaries": [
                {
                    "TeamID": "XXXXXXXXXX",
                    "SigningID": "com.example.app"
                },
                {
                    "TeamID": "*APPLE*"
                }
            ],
            "DeniedBinaries": [
                {
                    "SigningID": "com.apple.MobileSMS"
                }
            ]
        }
    }
}
```

## See Also

- [Configuring managed apps and extensions](configuring-managed-apps-and-extensions.md)
  Provide managed apps and extensions with app configuration and secrets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/allowing-and-denying-apps-and-binaries)*