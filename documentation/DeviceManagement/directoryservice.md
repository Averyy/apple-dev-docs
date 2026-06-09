# DirectoryService

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures an Active Directory (AD) domain.

**Availability**:
- macOS 10.8+

## Declaration

```swift
object DirectoryService
```

#### Discussion

Specify `com.apple.DirectoryService.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | macOS |
| Allow multiple payloads | macOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>HostName</key>
            <string>host.example.com</string>
            <key>Password</key>
            <string>Password123</string>
            <key>UserName</key>
            <string>bind</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mydspayload</string>
            <key>PayloadType</key>
            <string>com.apple.DirectoryService.managed</string>
            <key>PayloadUUID</key>
            <string>bb657e20-60b9-4c47-8730-51803ddf69e7</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Active Directory</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>079b6bc3-4356-4d80-89b4-a4b8a82eb739</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `ADAllowMultiDomainAuth` (boolean): If `true`, the system allows authentication from any domain in the namespace.
- `ADAllowMultiDomainAuthFlag` (boolean): If `true`, the system enables the `ADAllowMultiDomainAuth` key. Available: macOS 10.9+
- `ADCreateMobileAccountAtLogin` (boolean): If `true`, the system creates a mobile account at login.
- `ADCreateMobileAccountAtLoginFlag` (boolean): If `true`, the system enables the `ADCreateMobileAccountAtLogin` key. Available: macOS 10.9+
- `ADDefaultUserShell` (string): The default user shell.
- `ADDefaultUserShellFlag` (boolean): If `true`, the system enables the `ADDefaultUserShell` key.
- `ADDomainAdminGroupList` ([string]): The list of Active Directory groups with admin access.
- `ADDomainAdminGroupListFlag` (boolean): If `true`, the system enables the `ADDomainAdminGroupList` key.
- `ADForceHomeLocal` (boolean): If `true`, the system forces a local home directory.
- `ADForceHomeLocalFlag` (boolean): If `true`, the system enables the `ADForceHomeLocal` key. Available: macOS 10.9+
- `ADMapGGIDAttribute` (string): The map group GID to attribute.
- `ADMapGGIDAttributeFlag` (boolean): If `true`, the system enables the `ADMapGGIDAttributeFlag` key.
- `ADMapGIDAttribute` (string): The map GID to attribute.
- `ADMapGIDAttributeFlag` (boolean): If `true`, the system enables the `ADMapGIDAttribute` key.
- `ADMapUIDAttribute` (string): The map UID to attribute.
- `ADMapUIDAttributeFlag` (boolean): If `true`, the system enables the `ADMapUIDAttribute` key.
- `ADMountStyle` (string): The network home protocol to use: `afp` or `smb`.
- `ADNamespace` (string): The primary user account naming convention; either `forest` or `domain`.
- `ADNamespaceFlag` (boolean): If `true`, the system enables the `ADNamespace` key.
- `ADOrganizationalUnit` (string): The organizational unit to add the joining computer object to.
- `ADPacketEncrypt` (string): The packet encryption policy.
- `ADPacketEncryptFlag` (boolean): If `true`, the system enables the `ADPacketEncrypt` key.
- `ADPacketSign` (string): The packet signing policy.
- `ADPacketSignFlag` (boolean): If `true`, the system enables the `ADPacketSign` key.
- `ADPreferredDCServer` (string): The preferred domain server.
- `ADPreferredDCServerFlag` (boolean): If `true`, the system enables the `ADPreferredDCServer` key.
- `ADRestrictDDNS` ([string]): An array of strings that represent the interfaces allowed for dynamic DNS updates, such as en0 and en1.
- `ADRestrictDDNSFlag` (boolean): If `true`, the system enables the `ADRestrictDDNS` key.
- `ADTrustChangePassIntervalDays` (integer): The number of days before requiring a change of the computer trust account password. Set to `0` to disable the feature.
- `ADTrustChangePassIntervalDaysFlag` (boolean): If `true`, the system enables the `ADTrustChangePassIntervalDays` key.
- `ADUseWindowsUNCPath` (boolean): If `true`, the system uses the UNC path from Active Directory to derive the network home location.
- `ADUseWindowsUNCPathFlag` (boolean): If `true`, the system enables the `ADUseWindowsUNCPath` key. Available: macOS 10.9+
- `ADWarnUserBeforeCreatingMA` (boolean): If `true`, the system enables the warning before creating the mobile account.
- `ADWarnUserBeforeCreatingMAFlag` (boolean): If `true`, the system enables the `ADWarnUserBeforeCreatingMA` key. Available: macOS 10.9+
- `ClientID` (string): The client’s identifier.
- `Description` (string): The directory service description.
- `HostName` (string) *(required)*: The Active Directory domain to join.
- `Password` (string): The password of the account for the domain.
- `UserName` (string): The user name of the account for the domain.

## See Also

- [object ExtensibleSingleSignOn](extensiblesinglesignon.md)
  The payload that configures an app extension that performs single sign-on (SSO).
- [object ExtensibleSingleSignOnKerberos](extensiblesinglesignonkerberos.md)
  The payload that configures an app extension that performs single sign-on with the Kerberos extension.
- [object Identification](identification.md)
  The payload that configures the names of the account user.
- [object IdentityPreference](identitypreference.md)
  The payload that configures the user’s identity on the device.
- [object SingleSignOn](singlesignon.md)
  The payload that configures single sign-on (SSO).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/directoryservice)*