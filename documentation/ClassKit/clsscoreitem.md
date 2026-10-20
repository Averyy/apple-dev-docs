# CLSScoreItem

**Framework**: ClassKit  
**Kind**: class  
**Role**: Class

Activity information that signifies a score out of a possible maximum.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CLSScoreItem
```

```objc
@interface CLSScoreItem : CLSActivityItem
```

#### Overview

Use an activity item of this type to indicate the relative success in completing a task, like the number of correctly answered questions on a quiz.

## Topics

### Creating Score Activity Items
- [init(identifier: String, title: String, score: Double, maxScore: Double)](./clsscoreitem/init%28identifier,title,score,maxscore%29.md)
  Initializes an activity item that holds a score value.
### Managing the Score
- [var score: Double](./clsscoreitem/score.md)
  The score earned by a user in completing the task.
- [var maxScore: Double](./clsscoreitem/maxscore.md)
  The maximum possible score that the user can earn on a given task.

## Relationships

### Inherits From
- [CLSActivityItem](./clsactivityitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Activity items
- [Recording additional metrics about a completed task](./recording-additional-metrics-about-a-completed-task.md)
  Add an activity item to an activity to record additional information about a student’s attempt to complete a task.
- [class CLSBinaryItem](./clsbinaryitem.md)
  Activity information that is true or false, pass or fail, yes or no.
- [class CLSQuantityItem](./clsquantityitem.md)
  Activity information that signifies a quantity.
- [class CLSActivityItem](./clsactivityitem.md)
  An abstract base class for gathering information about an activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsscoreitem)*