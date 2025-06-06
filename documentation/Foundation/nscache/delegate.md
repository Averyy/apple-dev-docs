# delegate

**Framework**: Foundation  
**Kind**: property

The cache’s delegate.

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
unowned(unsafe) var delegate: (any NSCacheDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`NSCacheDelegate`](nscachedelegate.md) protocol.

## See Also

- [protocol NSCacheDelegate](nscachedelegate.md)
  The delegate of an [`NSCache`](nscache.md) object implements this protocol to perform specialized actions when an object is about to be evicted or removed from the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache/delegate)*