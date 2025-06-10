# NSRelativeSpecifier

**Framework**: Foundation  
**Kind**: class

A specifier that indicates an object in a collection by its position relative to another object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSRelativeSpecifier
```

#### Overview

You don’t normally subclass `NSRelativeSpecifier`.

## Topics

### Initializing a relative specifier
- [init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String, relativePosition: NSRelativeSpecifier.RelativePosition, baseSpecifier: NSScriptObjectSpecifier?)](nsrelativespecifier/init(containerclassdescription:containerspecifier:key:relativeposition:basespecifier:).md)
  Invokes the super class’s [`init(containerClassDescription:containerSpecifier:key:)`](nsscriptobjectspecifier/init(containerclassdescription:containerspecifier:key:).md) method and initializes the relative position and base specifier to `relPos` and `baseSpecifier`.
### Accessing a relative specifier
- [var baseSpecifier: NSScriptObjectSpecifier?](nsrelativespecifier/basespecifier.md)
  Sets the specifier for the base object.
- [var relativePosition: NSRelativeSpecifier.RelativePosition](nsrelativespecifier/relativeposition-swift.property.md)
  Sets the relative position encapsulated by the receiver.
### Constants
- [NSRelativeSpecifier.RelativePosition](nsrelativespecifier/relativeposition-swift.enum.md)
  These constants are used by [`relativePosition`](nsrelativespecifier/relativeposition-swift.property.md) and [`relativePosition`](nsrelativespecifier/relativeposition-swift.property.md).
### Initializers
- [init?(coder: NSCoder)](nsrelativespecifier/init(coder:).md)

## Relationships

### Inherits From
- [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSScriptObjectSpecifier](nsscriptobjectspecifier.md)
  An abstract class used to represent natural language expressions.
- [class NSPropertySpecifier](nspropertyspecifier.md)
  A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [class NSPositionalSpecifier](nspositionalspecifier.md)
  A specifier for an insertion point in a container relative to another object in the container.
- [class NSRandomSpecifier](nsrandomspecifier.md)
  A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSRangeSpecifier](nsrangespecifier.md)
  A specifier for a range of objects in a container.
- [class NSUniqueIDSpecifier](nsuniqueidspecifier.md)
  A specifier for an object in a collection (or container) by unique ID.
- [class NSWhoseSpecifier](nswhosespecifier.md)
  A specifier that indicates every object in a collection matching a condition.
- [class NSNameSpecifier](nsnamespecifier.md)
  A specifier for an object in a collection (or container) by name.
- [class NSMiddleSpecifier](nsmiddlespecifier.md)
  A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSIndexSpecifier](nsindexspecifier.md)
  A specifier representing an object in a collection (or container) with an index number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrelativespecifier)*