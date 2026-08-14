# CLSActivityItem

**Framework**: ClassKit  
**Kind**: class

An abstract base class for gathering information about an activity.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CLSActivityItem
```

#### Overview

You don’t typically use an instance of this class directly. Instead, use one of its subclasses to represent a particular activity metric. For example, use a [`CLSScoreItem`](clsscoreitem.md) to add a score to a [`CLSContextType.quiz`](clscontexttype/quiz.md) activity.

## Topics

### Accessing Activity Item Information
- [var identifier: String](clsactivityitem/identifier.md)
  An identifier for the activity item.
- [var title: String](clsactivityitem/title.md)
  A human readable name for the activity item.

## Relationships

### Inherits From
- [CLSObject](clsobject.md)
### Inherited By
- [CLSBinaryItem](clsbinaryitem.md)
- [CLSQuantityItem](clsquantityitem.md)
- [CLSScoreItem](clsscoreitem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Recording additional metrics about a completed task](recording-additional-metrics-about-a-completed-task.md)
  Add an activity item to an activity to record additional information about a student’s attempt to complete a task.
- [class CLSScoreItem](clsscoreitem.md)
  Activity information that signifies a score out of a possible maximum.
- [class CLSBinaryItem](clsbinaryitem.md)
  Activity information that is true or false, pass or fail, yes or no.
- [class CLSQuantityItem](clsquantityitem.md)
  Activity information that signifies a quantity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivityitem)*