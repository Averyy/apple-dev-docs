# NSPurgeableData

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSPurgeableData : NSMutableData
```

#### Overview

[`NSPurgeableData`](./nspurgeabledata.md) objects inherit their creation methods from their superclass, [`NSMutableData`](./nsmutabledata.md) while providing a default implementation of the [`NSDiscardableContent`](./nsdiscardablecontent.md) protocol.

All [`NSPurgeableData`](./nspurgeabledata.md) objects begin “accessed” to ensure that they are not instantly discarded. The [`beginContentAccess()`](./nsdiscardablecontent/begincontentaccess%28%29.md) method marks the object’s bytes as “accessed,” thus protecting them from being discarded, and must be called before accessing the object, or else an exception will be raised. This method returns [`true`](../Swift/true.md) if the bytes have not been discarded and if they have been successfully marked as “accessed”. Any method that directly or indirectly accesses these bytes or their length when they are not “accessed” will raise an exception. When you are done with the data, call [`endContentAccess()`](./nsdiscardablecontent/endcontentaccess%28%29.md) to allow them to be discarded in order to quickly free up memory.

You may use these objects by themselves, and do not necessarily have to use them in conjunction with [`NSCache`](./nscache.md) to get the purging behavior. The [`NSCache`](./nscache.md) class incorporates a caching mechanism with some auto-removal policies to ensure that its memory footprint does not get too large.

[`NSPurgeableData`](./nspurgeabledata.md) objects should not be used as keys in hashing-based collections, because the value of the bytes pointer can change after every mutation of the data.

## Relationships

### Inherits From
- [NSMutableData](./nsmutabledata.md)
### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [CVarArg](../Swift/cvararg.md)
- [Collection](../Swift/collection.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [DataProtocol](./dataprotocol.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSDiscardableContent](./nsdiscardablecontent.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Purgeable Collections
- [class NSCache](./nscache.md)
  A mutable collection you use to temporarily store transient key-value pairs that are subject to eviction when resources are low.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspurgeabledata)*