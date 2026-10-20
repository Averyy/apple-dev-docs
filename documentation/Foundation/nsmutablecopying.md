# NSMutableCopying

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

A protocol that mutable objects adopt to provide functional copies of themselves.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSMutableCopying
```

```objc
@protocol NSMutableCopying
```

#### Overview

The [`NSMutableCopying`](./nsmutablecopying.md) protocol declares a method for providing mutable copies of an object. Only classes that define an “immutable vs. mutable” distinction should adopt this protocol. Classes that don’t define such a distinction should adopt [`NSCopying`](./nscopying.md) instead.

[`NSMutableCopying`](./nsmutablecopying.md) declares one method, [`mutableCopy(with:)`](./nsmutablecopying/mutablecopy%28with%29.md), but mutable copying is commonly invoked with the convenience method [`mutableCopy()`](../ObjectiveC/nsobject-swift.class/mutablecopy%28%29.md). The [`mutableCopy()`](../ObjectiveC/nsobject-swift.class/mutablecopy%28%29.md) method is defined for all NSObjects and simply invokes [`mutableCopy(with:)`](./nsmutablecopying/mutablecopy%28with%29.md) with the default zone.

If a subclass inherits [`NSMutableCopying`](./nsmutablecopying.md) from its superclass and declares additional instance variables, the subclass has to override [`mutableCopy(with:)`](./nsmutablecopying/mutablecopy%28with%29.md) to properly handle its own instance variables, invoking the superclass’s implementation first.

## Topics

### Copying
- [func mutableCopy(with: NSZone?) -> Any](./nsmutablecopying/mutablecopy%28with%29.md)
  Returns a new instance that’s a mutable copy of the receiver.

## Relationships

### Conforming Types
- [NSArray](./nsarray.md)
- [NSAttributedString](./nsattributedstring.md)
- [NSCharacterSet](./nscharacterset.md)
- [NSCountedSet](./nscountedset.md)
- [NSData](./nsdata.md)
- [NSDictionary](./nsdictionary.md)
- [NSIndexSet](./nsindexset.md)
- [NSMutableArray](./nsmutablearray.md)
- [NSMutableAttributedString](./nsmutableattributedstring.md)
- [NSMutableCharacterSet](./nsmutablecharacterset.md)
- [NSMutableData](./nsmutabledata.md)
- [NSMutableDictionary](./nsmutabledictionary.md)
- [NSMutableIndexSet](./nsmutableindexset.md)
- [NSMutableOrderedSet](./nsmutableorderedset.md)
- [NSMutableSet](./nsmutableset.md)
- [NSMutableString](./nsmutablestring.md)
- [NSMutableURLRequest](./nsmutableurlrequest.md)
- [NSOrderedSet](./nsorderedset.md)
- [NSPurgeableData](./nspurgeabledata.md)
- [NSSet](./nsset.md)
- [NSString](./nsstring.md)
- [NSURLRequest](./nsurlrequest.md)

## See Also

### Copying
- [protocol NSCopying](./nscopying.md)
  A protocol that objects adopt to provide functional copies of themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecopying)*