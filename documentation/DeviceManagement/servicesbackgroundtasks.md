# ServicesBackgroundTasks

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure background tasks.

**Availability**:
- macOS 15.0+

## Declaration

```swift
object ServicesBackgroundTasks
```

#### Discussion

Specify `com.apple.configuration.services.background-tasks` as the declaration type.

One or both of `ExecutableAssetReference` or `LaunchdConfigurations` needs to be present.

If `ExecutableAssetReference` is present, the POSIX permissions of the files in the zip archive need to be set correctly. For example, executables must have the “x” bit set.

If `LaunchdConfigurations` is present, the device stores the launchd configuration files in a secure location and loads them into launchd. When the device updates a launchd configuration, it kills and restarts any associated running tasks.

If both `ExecutableAssetReference` and `LaunchdConfigurations` are present, and the device changes just the executable data, it kills and restarts any running tasks associated with the launchd configurations.

> **Note**:  If an executable is an app, the device can’t manage the app as it can only manage apps installed in `/Applications`. Also, the device can’t use system extensions in the app as it only loads them from apps installed in `/Applications`.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are applied separately |

##### Configuration Example

This configuration sets up a background task using a launchd daemon.

```json
{
    "Type": "com.apple.configuration.services.background-tasks",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "TaskType": "com.example.bgtask",
        "TaskDescription": "Test script",
        "ExecutableAssetReference": "5840A1CB-A769-4C08-8968-13E8BA705B3E",
        "LaunchdConfigurations": [
            {
                "FileAssetReference": "F6A59159-FFA5-4DA9-B2E8-316AC4C99C78",
                "Context": "daemon"
            }
        ]
    }
}
```

## Topics

### Objects
- [object ServicesBackgroundTasksLaunchdItemObject](servicesbackgroundtaskslaunchditemobject.md)
  A dictionary of launchd configurations.

## Properties

- `ExecutableAssetReference` (string): Specifies the identifier of an asset declaration containing a reference to the files to be used for the background task configuration. The corresponding asset must be of type `com.apple.asset.data`. The referenced data must be a zip archive of an entire directory that the device expands and stores in a well known location for the background task. The asset’s “ContentType” and “Hash-SHA-256” keys in the “Reference” key are required. This zip archive should contain background task executables, scripts, and configuration files, but not the `launchd` configuration files. The device stores the expanded zip archive in the tamper-proof `/var/db/ManagedConfigurationFiles/BackgroundTaskServices/Services/<TaskType>` directory, where `<TaskType>` is the value of the `TaskType` key in the configuration.
- `LaunchdConfigurations` ([ServicesBackgroundTasksLaunchdItemObject]): An array of `launchd` configuration files used to run the background tasks. The device stores the configuration files in the tamper-proof `/var/db/ManagedConfigurationFiles/BackgroundTaskServices/LaunchDaemons` or `/var/db/ManagedConfigurationFiles/BackgroundTaskServices/LaunchAgents` directories, based on the `Context` value for each item.
- `TaskDescription` (string): A description of the set of background tasks this configuration manages.
- `TaskType` (string) *(required)*: The unique identifier of the set of background tasks managed with this configuration. This should be a reverse DNS style identifier. The device uses this identifier to differentiate between tasks in different configurations.

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
- [object AppSettings](appsettings.md)
  The declaration to configure app settings.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object ContentCaching](contentcaching.md)
  The declaration to configure the Content Caching service.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExtensibleSSO](extensiblesso.md)
  The declaration to configure Extensible Single Sign-On.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/servicesbackgroundtasks)*