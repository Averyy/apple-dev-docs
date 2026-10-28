# NSUniqueIDSpecifier

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A specifier for an object in a collection (or container) by unique ID.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSUniqueIDSpecifier
```

```objc
@interface NSUniqueIDSpecifier : NSScriptObjectSpecifier
```

## Overview

This specifier works only for objects that have an ID property. The unique ID object passed to an instance of  `NSUniqueIDSpecifier` must be either an `NSNumber` object or an `NSString` object. The exact type should match the scripting dictionary declaration of the ID attribute for the relevant scripting class.

You can expect that the ID property will be *read only* for any object that supports it. Therefore a scripter can obtain the unique ID for an object and refer to the object by the ID, but cannot set the unique ID.

You don’t normally subclass `NSUniqueIDSpecifier`.

The evaluation of `NSUniqueIDSpecifier` objects follows these steps until the specified object is found:

1. If the container implements a method whose selector matches the relevant `valueIn<Key>WithUniqueID:` pattern established by scripting key-value coding, the method is invoked. This method can potentially be very fast, and it may be relatively easy to implement.
2. As is the case when evaluating any script object specifier, the container of the specified object is given a chance to evaluate the object specifier. If the container class implements the [`indicesOfObjects(byEvaluatingObjectSpecifier:)`](../ObjectiveC/nsobject-swift.class/indicesofobjects%28byevaluatingobjectspecifier%29.md) method, the method is invoked. This method can potentially be very fast, but it is relatively difficult to implement.
3. An [`NSWhoseSpecifier`](./nswhosespecifier.md) object that specifies the first object whose relevant `'ID  '` attribute matches the ID is synthesized and evaluated. The `NSWhoseSpecifier` object must search through all of the keyed elements in the container, looking for a match. The search is potentially very slow.

## Topics

### Initializing a unique ID specifier
- [init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String, uniqueID: Any)](./nsuniqueidspecifier/init%28containerclassdescription,containerspecifier,key,uniqueid%29.md)
  Returns an `NSUniqueIDSpecifier` object, initialized with the given arguments.
### Accessing unique ID information
- [var uniqueID: Any](./nsuniqueidspecifier/uniqueid.md)
  Returns the ID encapsulated by the receiver.
### Initializers
- [init?(coder: NSCoder)](./nsuniqueidspecifier/init%28coder%29.md)

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
- [class NSRangeSpecifier](./nsrangespecifier.md)
  A specifier for a range of objects in a container.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier)*