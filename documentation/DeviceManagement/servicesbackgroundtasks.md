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

> **Note**:  If an executable is an app, the system can’t manage the app as it can only manage apps installed in `/Applications`. Also, the system can’t use system extensions in the app as it only loads them from apps installed in `/Applications`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/servicesbackgroundtasks)*