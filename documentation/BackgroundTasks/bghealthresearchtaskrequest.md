# BGHealthResearchTaskRequest

**Framework**: Background Tasks  
**Kind**: class

A request to launch your app in the background to execute processing for a health research study in which a user participates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class BGHealthResearchTaskRequest
```

## Mentions

- [Choosing Background Strategies for Your App](choosing-background-strategies-for-your-app.md)

## Topics

### Setting file permissions
- [var protectionTypeOfRequiredData: NSString](bghealthresearchtaskrequest/protectiontypeofrequireddata.md)
  The file protection required to access health research data relevant to complete the task.

## Relationships

### Inherits From
- [BGProcessingTaskRequest](bgprocessingtaskrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BGProcessingTaskRequest](bgprocessingtaskrequest.md)
  A request to launch your app in the background to execute a processing task that can take minutes to complete.
- [class BGAppRefreshTaskRequest](bgapprefreshtaskrequest.md)
  A request to launch your app in the background to execute a short refresh task.
- [class BGTaskRequest](bgtaskrequest.md)
  An abstract class for representing task requests.
- [class BGContinuedProcessingTaskRequest](bgcontinuedprocessingtaskrequest.md)
  A request for a workload that the system continues processing even if a person backgrounds the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bghealthresearchtaskrequest)*