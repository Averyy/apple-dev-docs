# StatusServicesBackgroundTaskBackgroundTask_Launchd_DeviceManagementObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that indicates a [`ServicesBackgroundTasks`](servicesbackgroundtasks.md) configuration created this background task. The dictionary contains properties that identify the configuration and the declaration asset that provided the launchd plist for the task.

**Availability**:
- macOS 15.0+

## Declaration

```swift
object StatusServicesBackgroundTaskBackgroundTask_Launchd_DeviceManagementObject
```

## Properties

- `asset-identifier` (string) *(required)*: The `Identifier` of the declaration asset that provided the launchd plist for this task.
- `asset-server-token` (string) *(required)*: The `ServerToken` of the declaration asset that provided the launchd plist for this task.
- `configuration-identifier` (string) *(required)*: The identifier of the [`ServicesBackgroundTasks`](servicesbackgroundtasks.md) configuration that created this task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusservicesbackgroundtaskbackgroundtask_launchd_devicemanagementobject)*