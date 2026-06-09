# StatusServicesBackgroundTaskBackgroundTaskObject

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports a background task.

**Availability**:
- macOS 14.0+

## Declaration

```swift
object StatusServicesBackgroundTaskBackgroundTaskObject
```

## Topics

### Objects
- [object StatusServicesBackgroundTaskBackgroundTask_LaunchdObject](statusservicesbackgroundtaskbackgroundtask_launchdobject.md)
  Details about a `launchd`-based background task, which is only present when the type is `daemon` or `agent`.

## Properties

- `_removed` (boolean): If `true`, the system removed the background task and the status item object only contains this key and the `identifier` key.
- `code-signature` (string): For types other than `agent` or `daemon`, this is the code signature designated requirement of the item, if available.
- `identifier` (string) *(required)*: The background task UUID which the system uses as the primary key.
- `launchd` (StatusServicesBackgroundTaskBackgroundTask_LaunchdObject): Details about a `launchd`-based background task, which is only present when the type is `daemon` or `agent`.
- `path` (string) *(required)*: For an `agent` or `daemon`, the path to the `launchd` `plist` file. For other types, the path to the app or the document.
- `state` (string) *(required)*: The [`SMAppService.Status`](https://developer.apple.com/documentation/ServiceManagement/SMAppService/Status-swift.enum) enumeration.
- `type` (string) *(required)*: The daemon, agent, or SFL login item type.
- `uid` (integer) *(required)*: The numeric user identifier of the owner of the background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusservicesbackgroundtaskbackgroundtaskobject)*