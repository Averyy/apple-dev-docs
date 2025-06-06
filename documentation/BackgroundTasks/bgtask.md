# BGTask

**Framework**: Background Tasks  
**Kind**: class

An abstract class representing a task that’s run while the app is in the background.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class BGTask
```

## Topics

### Reading Task Information
- [var identifier: String](bgtask/identifier.md)
  The string identifier of the task.
### Configuring a Task
- [var expirationHandler: (() -> Void)?](bgtask/expirationhandler.md)
  A handler called shortly before the task’s background time expires.
- [func setTaskCompleted(success: Bool)](bgtask/settaskcompleted(success:).md)
  Informs the background task scheduler that the task is complete.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [BGAppRefreshTask](bgapprefreshtask.md)
- [BGProcessingTask](bgprocessingtask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BGProcessingTask](bgprocessingtask.md)
  A time-consuming processing task that runs while the app is in the background.
- [class BGAppRefreshTask](bgapprefreshtask.md)
  An object representing a short task typically used to refresh content that’s run while the app is in the background.
- [class BGHealthResearchTask](bghealthresearchtask.md)
  A time-consuming, necessary processing task that runs while the app is in the background to prepare data essential to a health research study.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtask)*