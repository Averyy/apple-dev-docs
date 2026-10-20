# BGTaskRequest

**Framework**: Background Tasks  
**Kind**: class  
**Role**: Class

An abstract class for representing task requests.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class BGTaskRequest
```

```objc
@interface BGTaskRequest : NSObject
```

## Topics

### Configuring a Task Request
- [var earliestBeginDate: Date?](./bgtaskrequest/earliestbegindate.md)
  The earliest date and time at which to run the task.
- [var identifier: String](./bgtaskrequest/identifier.md)
  The identifier of the task associated with the request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [BGAppRefreshTaskRequest](./bgapprefreshtaskrequest.md)
- [BGContinuedProcessingTaskRequest](./bgcontinuedprocessingtaskrequest.md)
- [BGProcessingTaskRequest](./bgprocessingtaskrequest.md)
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
- [class BGAppRefreshTaskRequest](./bgapprefreshtaskrequest.md)
  A request to launch your app in the background to execute a short refresh task.
- [class BGHealthResearchTaskRequest](./bghealthresearchtaskrequest.md)
  A request to launch your app in the background to execute processing for a health research study in which a user participates.
- [class BGContinuedProcessingTaskRequest](./bgcontinuedprocessingtaskrequest.md)
  A request for a workload that the system continues processing even if a person backgrounds the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskrequest)*