# BGAppRefreshTaskRequest

**Framework**: Background Tasks  
**Kind**: class  
**Role**: Class

A request to launch your app in the background to execute a short refresh task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class BGAppRefreshTaskRequest
```

```objc
@interface BGAppRefreshTaskRequest : BGTaskRequest
```

## Mentions

- [Choosing Background Strategies for Your App](./choosing-background-strategies-for-your-app.md)

## Topics

### Initializing a refresh task request
- [init(identifier: String)](./bgapprefreshtaskrequest/init%28identifier%29.md)
  Return a new refresh task request for the specified identifier.

## Relationships

### Inherits From
- [BGTaskRequest](./bgtaskrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Task requests
- [class BGProcessingTaskRequest](./bgprocessingtaskrequest.md)
  A request to launch your app in the background to execute a processing task that can take minutes to complete.
- [class BGTaskRequest](./bgtaskrequest.md)
  An abstract class for representing task requests.
- [class BGHealthResearchTaskRequest](./bghealthresearchtaskrequest.md)
  A request to launch your app in the background to execute processing for a health research study in which a user participates.
- [class BGContinuedProcessingTaskRequest](./bgcontinuedprocessingtaskrequest.md)
  A request for a workload that the system continues processing even if a person backgrounds the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgapprefreshtaskrequest)*