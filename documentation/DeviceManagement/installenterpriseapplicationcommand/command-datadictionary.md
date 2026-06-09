# InstallEnterpriseApplicationCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to install an enterprise app on a device.

**Availability**:
- macOS 10.13.6+

## Declaration

```swift
object InstallEnterpriseApplicationCommand.Command
```

## Topics

### Objects
- [object InstallEnterpriseApplicationCommand.Command.Configuration](installenterpriseapplicationcommand/command-data.dictionary/configuration-data.dictionary.md)
  A dictionary that contains the configuration to install an enterprise app.
- [object InstallEnterpriseApplicationCommand.Command.Manifest](installenterpriseapplicationcommand/command-data.dictionary/manifest-data.dictionary.md)
  A dictionary that contains a manifest.

## Properties

- `ChangeManagementState` (string): The change management state. This value doesn’t work with the user enrollments. The only possible value is: - `Managed`: Take management of the app if the user installed it already and `InstallAsManaged` is `true`. Available: macOS 11+
- `Configuration` (InstallEnterpriseApplicationCommand.Command.Configuration): A dictionary that contains the initial configuration of the app, if you choose to provide it. Available: macOS 11+
- `InstallAsManaged` (boolean): If `true`, install the app as a managed app. Otherwise, the system installs the app as unmanaged. If you reinstall a manged app and omit this value or set it to `false`, the app becomes unmanaged. For manifest-based installs, if `true`, the system only considers apps installed in `/Applications` as managed. In macOS 11 through 13, the system requires that the `pkg` only contains a single signed app. Available: macOS 11+
- `iOSApp` (boolean): If `true`, the app is an iOS app that can run on a Mac with Apple silicon in macOS 11 and later. Available: macOS 11+
- `ManagementFlags` (integer): The management flags. The possible values are: - `1`: If `InstallAsManaged` is `true`, remove the app upon removal of the MDM profile. Available: macOS 11+
- `Manifest` (InstallEnterpriseApplicationCommand.Command.Manifest): A dictionary that specifies where to download the app. This value uses the [`ManifestURL`](manifesturl.md) format.
- `ManifestURL` (string): The URL of the app manifest, which needs to begin with `https:`. The manifest is returned as a property list that uses the [`ManifestURL`](manifesturl.md) format.
- `ManifestURLPinningCerts` ([data]): An array of DER-encoded certificates to pin the connection when fetching the `ManifestURL`.
- `PinningRevocationCheckRequired` (boolean): If `true`, certificate revocation checks require a positive response when using certificate pinning with `ManifestURLPinningCerts`.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installenterpriseapplicationcommand/command-data.dictionary)*