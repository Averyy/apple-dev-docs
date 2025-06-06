# NSCacheDelegate

**Framework**: Foundation  
**Kind**: protocol

The delegate of an [`NSCache`](nscache.md) object implements this protocol to perform specialized actions when an object is about to be evicted or removed from the cache.

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
protocol NSCacheDelegate : NSObjectProtocol
```

## Topics

### Responding to Object Eviction
- [func cache(NSCache<AnyObject, AnyObject>, willEvictObject: Any)](nscachedelegate/cache(_:willevictobject:).md)
  Called when an object is about to be evicted or removed from the cache.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSCacheDelegate)?](nscache/delegate.md)
  The cache’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscachedelegate)*