# CLSBinaryItem

**Framework**: ClassKit  
**Kind**: class

Activity information that is true or false, pass or fail, yes or no.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CLSBinaryItem
```

#### Overview

Use an activity item of this type to indicate a binary condition, such as whether a student passed a test or failed it. Set the [`valueType`](clsbinaryitem/valuetype.md) property to specify how the binary condition should be reported to a teacher.

## Topics

### Creating Binary Activity Items
- [init(identifier: String, title: String, type: CLSBinaryValueType)](clsbinaryitem/init(identifier:title:type:).md)
  Initializes a new binary activity item of the given type.
- [enum CLSBinaryValueType](clsbinaryvaluetype.md)
  The kinds of outcomes that a binary activity item can represent.
### Managing the Value
- [var value: Bool](clsbinaryitem/value.md)
  The value that the binary activity item takes.
- [var valueType: CLSBinaryValueType](clsbinaryitem/valuetype.md)
  The kind of outcome that the binary activity item represents.

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
- [class CLSQuantityItem](clsquantityitem.md)
  Activity information that signifies a quantity.
- [class CLSActivityItem](clsactivityitem.md)
  An abstract base class for gathering information about an activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsbinaryitem)*