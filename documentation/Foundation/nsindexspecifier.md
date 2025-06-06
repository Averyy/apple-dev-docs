# NSIndexSpecifier

**Framework**: Foundation  
**Kind**: class

A specifier representing an object in a collection (or container) with an index number.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSIndexSpecifier
```

#### Overview

The script terms `first` and `front` specify the object with index `0`, while `last` specifies the object with index of `count-1`. A negative index indicates a location by counting backward from the last object in the collection.

You don’t normally subclass `NSIndexSpecifier`.

## Topics

### Creating Index Specifiers
- [init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String, index: Int)](nsindexspecifier/init(containerclassdescription:containerspecifier:key:index:).md)
  Initializes an allocated [`NSIndexSpecifier`](nsindexspecifier.md) object with a class description, container specifier, collection key, and object index.
### Accessing the Index
- [var index: Int](nsindexspecifier/index.md)
  Sets the value of the receiver’s `index` property.

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
- [class NSRelativeSpecifier](nsrelativespecifier.md)
  A specifier that indicates an object in a collection by its position relative to another object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexspecifier)*