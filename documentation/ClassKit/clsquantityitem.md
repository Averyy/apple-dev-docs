# CLSQuantityItem

**Framework**: ClassKit  
**Kind**: class

Activity information that signifies a quantity.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CLSQuantityItem
```

#### Overview

Use an activity item of this type to associate a discrete value with a task. For example, you might use it to indicate how many times the user requested a hint while taking a quiz.

## Topics

### Creating Quantity Activity Items
- [init(identifier: String, title: String)](clsquantityitem/init(identifier:title:).md)
  Initializes an activity item that records a discrete quantity.
### Managing the Quantity
- [var quantity: Double](clsquantityitem/quantity.md)
  A quantity associated with the task.

## Relationships

### Inherits From
- [CLSActivityItem](clsactivityitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Recording additional metrics about a completed task](recording-additional-metrics-about-a-completed-task.md)
  Add an activity item to an activity to record additional information about a student’s attempt to complete a task.
- [class CLSScoreItem](clsscoreitem.md)
  Activity information that signifies a score out of a possible maximum.
- [class CLSBinaryItem](clsbinaryitem.md)
  Activity information that is true or false, pass or fail, yes or no.
- [class CLSActivityItem](clsactivityitem.md)
  An abstract base class for gathering information about an activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsquantityitem)*