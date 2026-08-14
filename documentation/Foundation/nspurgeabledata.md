# NSPurgeableData

**Framework**: Foundation  
**Kind**: class

A mutable data object containing bytes that can be discarded when they’re no longer needed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSPurgeableData
```

#### Overview

[`NSPurgeableData`](nspurgeabledata.md) objects inherit their creation methods from their superclass, [`NSMutableData`](nsmutabledata.md) while providing a default implementation of the [`NSDiscardableContent`](nsdiscardablecontent.md) protocol.

All [`NSPurgeableData`](nspurgeabledata.md) objects begin “accessed” to ensure that they are not instantly discarded. The [`beginContentAccess()`](nsdiscardablecontent/begincontentaccess().md) method marks the object’s bytes as “accessed,” thus protecting them from being discarded, and must be called before accessing the object, or else an exception will be raised. This method returns [`true`](https://developer.apple.com/documentation/swift/true) if the bytes have not been discarded and if they have been successfully marked as “accessed”. Any method that directly or indirectly accesses these bytes or their length when they are not “accessed” will raise an exception. When you are done with the data, call [`endContentAccess()`](nsdiscardablecontent/endcontentaccess().md) to allow them to be discarded in order to quickly free up memory.

You may use these objects by themselves, and do not necessarily have to use them in conjunction with [`NSCache`](nscache.md) to get the purging behavior. The [`NSCache`](nscache.md) class incorporates a caching mechanism with some auto-removal policies to ensure that its memory footprint does not get too large.

[`NSPurgeableData`](nspurgeabledata.md) objects should not be used as keys in hashing-based collections, because the value of the bytes pointer can change after every mutation of the data.

## Relationships

### Inherits From
- [NSMutableData](nsmutabledata.md)
### Conforms To
- [BidirectionalCollection](../swift/bidirectionalcollection.md)
- [CVarArg](../swift/cvararg.md)
- [Collection](../swift/collection.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [DataProtocol](dataprotocol.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSDiscardableContent](nsdiscardablecontent.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [RandomAccessCollection](../swift/randomaccesscollection.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)

## See Also

- [class NSCache](nscache.md)
  A mutable collection you use to temporarily store transient key-value pairs that are subject to eviction when resources are low.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspurgeabledata)*