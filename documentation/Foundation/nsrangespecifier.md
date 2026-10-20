# NSRangeSpecifier

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A specifier for a range of objects in a container.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSRangeSpecifier
```

```objc
@interface NSRangeSpecifier : NSScriptObjectSpecifier
```

#### Overview

An `NSRangeSpecifier` object specifies a range (that is, an uninterrupted series) of objects in a container through two delimiting objects. The range is represented by two object specifiers, a start specifier and an end specifier, which can be of any specifier type (such as [`NSIndexSpecifier`](./nsindexspecifier.md) or [`NSWhoseSpecifier`](./nswhosespecifier.md) object). These specifiers are evaluated in the context of the same container object as the range specifier itself.

You don’t normally subclass `NSRangeSpecifier`.

## Topics

### Initializing a range specifier
- [init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String, start: NSScriptObjectSpecifier?, end: NSScriptObjectSpecifier?)](./nsrangespecifier/init%28containerclassdescription,containerspecifier,key,start,end%29.md)
  Returns a range specifier initialized with the given properties.
### Accessing a range specifier
- [var endSpecifier: NSScriptObjectSpecifier?](./nsrangespecifier/endspecifier.md)
  Sets the object specifier representing the last object of the range to a given object.
- [var startSpecifier: NSScriptObjectSpecifier?](./nsrangespecifier/startspecifier.md)
  Returns the object specifier representing the first object of the range.
### Initializers
- [init?(coder: NSCoder)](./nsrangespecifier/init%28coder%29.md)
- [init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String, startSpecifier: NSScriptObjectSpecifier?, endSpecifier: NSScriptObjectSpecifier?)](./nsrangespecifier/init%28containerclassdescription,containerspecifier,key,startspecifier,endspecifier%29.md)

## Relationships

### Inherits From
- [NSScriptObjectSpecifier](./nsscriptobjectspecifier.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Object Specifiers
- [class NSScriptObjectSpecifier](./nsscriptobjectspecifier.md)
  An abstract class used to represent natural language expressions.
- [class NSPropertySpecifier](./nspropertyspecifier.md)
  A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [class NSPositionalSpecifier](./nspositionalspecifier.md)
  A specifier for an insertion point in a container relative to another object in the container.
- [class NSRandomSpecifier](./nsrandomspecifier.md)
  A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSUniqueIDSpecifier](./nsuniqueidspecifier.md)
  A specifier for an object in a collection (or container) by unique ID.
- [class NSWhoseSpecifier](./nswhosespecifier.md)
  A specifier that indicates every object in a collection matching a condition.
- [class NSNameSpecifier](./nsnamespecifier.md)
  A specifier for an object in a collection (or container) by name.
- [class NSMiddleSpecifier](./nsmiddlespecifier.md)
  A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [class NSIndexSpecifier](./nsindexspecifier.md)
  A specifier representing an object in a collection (or container) with an index number.
- [class NSRelativeSpecifier](./nsrelativespecifier.md)
  A specifier that indicates an object in a collection by its position relative to another object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrangespecifier)*