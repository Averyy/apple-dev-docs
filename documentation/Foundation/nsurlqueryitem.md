# NSURLQueryItem

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object representing a single name/value pair for an item in the query portion of a URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSURLQueryItem
```

```objc
@interface NSURLQueryItem : NSObject
```

#### Overview

In Swift, this object bridges to [`URLQueryItem`](./urlqueryitem.md); use [`NSURLQueryItem`](./nsurlqueryitem.md) when you need reference semantics or other Foundation-specific behavior.

You use query items with the [`queryItems`](./nsurlcomponents/queryitems.md) property of an [`NSURLComponents`](./nsurlcomponents.md) object.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`URLQueryItem`](./urlqueryitem.md) structure, which bridges to the [`NSURLQueryItem`](./nsurlqueryitem.md) class. For more information about value types, see [Working with Foundation Types](../Swift/working-with-foundation-types.md).

## Topics

### Creating a Query Item
- [init(name: String, value: String?)](./nsurlqueryitem/init%28name,value%29.md)
  Initializes a newly allocated query item with the specified name and value.
### Reading a Query Item’s Name and Value
- [var name: String](./nsurlqueryitem/name.md)
  The name of the query item.
- [var value: String?](./nsurlqueryitem/value.md)
  The value for the query item.
### Initializers
- [init?(coder: NSCoder)](./nsurlqueryitem/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlqueryitem)*