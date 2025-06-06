# NSURLQueryItem

**Framework**: Foundation  
**Kind**: class

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

#### Overview

In Swift, this object bridges to [`URLQueryItem`](urlqueryitem.md); use [`NSURLQueryItem`](nsurlqueryitem.md) when you need reference semantics or other Foundation-specific behavior.

You use query items with the [`queryItems`](nsurlcomponents/queryitems.md) property of an [`NSURLComponents`](nsurlcomponents.md) object.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`URLQueryItem`](urlqueryitem.md) structure, which bridges to the [`NSURLQueryItem`](nsurlqueryitem.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`URLQueryItem`](urlqueryitem.md) structure, which bridges to the [`NSURLQueryItem`](nsurlqueryitem.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Creating a Query Item
- [init(name: String, value: String?)](nsurlqueryitem/init(name:value:).md)
  Initializes a newly allocated query item with the specified name and value.
### Reading a Query Item’s Name and Value
- [var name: String](nsurlqueryitem/name.md)
  The name of the query item.
- [var value: String?](nsurlqueryitem/value.md)
  The value for the query item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlqueryitem)*