# BGProcessingTaskRequest

**Framework**: Background Tasks  
**Kind**: class

A request to launch your app in the background to execute a processing task that can take minutes to complete.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class BGProcessingTaskRequest
```

## Topics

### Initializing a Processing Task Request
- [init(identifier: String)](bgprocessingtaskrequest/init(identifier:).md)
  Return a new processing task request for the specified identifier.
### Setting Task Request Options
- [var requiresExternalPower: Bool](bgprocessingtaskrequest/requiresexternalpower.md)
  A Boolean specifying if the processing task requires a device connected to power.
- [var requiresNetworkConnectivity: Bool](bgprocessingtaskrequest/requiresnetworkconnectivity.md)
  A Boolean specifying if the processing task requires network connectivity.

## Relationships

### Inherits From
- [BGTaskRequest](bgtaskrequest.md)
### Inherited By
- [BGHealthResearchTaskRequest](bghealthresearchtaskrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BGAppRefreshTaskRequest](bgapprefreshtaskrequest.md)
  A request to launch your app in the background to execute a short refresh task.
- [class BGTaskRequest](bgtaskrequest.md)
  An abstract class for representing task requests.
- [class BGHealthResearchTaskRequest](bghealthresearchtaskrequest.md)
  A request to launch your app in the background to execute processing for a health research study in which a user participates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgprocessingtaskrequest)*