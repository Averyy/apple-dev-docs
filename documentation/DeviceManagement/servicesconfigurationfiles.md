# ServicesConfigurationFiles

**Framework**: Device Management  
**Kind**: dictionary

The managed configuration files for services.

**Availability**:
- macOS 14.0+

## Declaration

```swift
object ServicesConfigurationFiles
```

#### Discussion

Specify `com.apple.configuration.services.configuration-files` as the declaration type.

The device stores the service configurations files from this configuration in a tamper-proof location. Built-in services use these files to override their default configurations.

The `DataAssetReference` refers to a zip archive that contains configuration files for a specific service. When the device applies the configuration, it downloads the asset data and expands the archive into a service-specific location. If the device updates a configuration, it downloads the new asset data and expands the data to replace what it previously installed. If the device deactivates or removes the configuration, it removes the configuration files from the service-specific directory.

All files in the expanded archive are set to -r–r–r– unix file permissions. Any links in the archive will be restricted to referencing files within the service-specific location.

The following built-in system services use managed configuration files:

| ServiceType | Manages |
| --- | --- |
| com.apple.sshd | /etc/ssh |
| com.apple.sudo | /etc/sudoers |
| com.apple.pam | /etc/pam.d |
| com.apple.cups | /etc/cups |
| com.apple.apache.httpd | /etc/apache2 |
| com.apple.bash | /etc/profile |
| com.apple.zsh | /etc/zprofile |
|  | /etc/zlogin |
|  | /etc/zlogout |
|  | /etc/zshenv |
|  | /etc/zshrc |
| com.apple.cryptoTokenKit | /etc/SmartcardLogin.plist |
| com.apple.authorization | /Library/Security/ |

The files in the zip archive need to mirror the folder structure and configuration files that the service expects to be present starting at the root of the file system. The service uses only the files the declaration provides and ignores the ones in its default directories.

For example, a configuration with `ServiceType`: `com.apple.sshd` configures sshd to use the files that the `DataAssetReference` provides, instead of the files located at /etc/ssh. The corresponding zip archive needs to contain:

```None
etc/
└ ssh/
  ├ moduli
  ├ ssh_config
  ├ ssh_config.d/
  ├ sshd_config
  └ sshd_config.d/
    └ 100-macos.conf
```

You can create an executable that uses service configuration files by calling the `mcf_service_path_for_service_type` method in the `libmanagedconfigurationfiles.dylib` system library. You pass in an identifier for your service type and the method returns the file system path for the directory that contains the corresponding service configuration files. Use those files to override the standard or default configuration the executable would otherwise use. See libmanagedconfigurationfiles.h in the macOS SDK for more detail.

> ❗ **Important**:  The system reserves the `com.apple` prefix for built-in services.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | macOS |
| Allowed in user scope | NA |

##### Configuration Example

```json
{
    "Type": "com.apple.configuration.services.configuration-files",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ServiceType": "com.openssh.sshd",
        "DataAssetReference": "168663D8-A06D-4C8A-93A4-AD225D85BF69"
    }
}
```

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a subscribed calendar.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.
- [object ManagementTest](managementtest.md)
  The declaration to test declarative device management.
- [object MathSettings](mathsettings.md)
  The declaration to configure the math and calculator apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/servicesconfigurationfiles)*