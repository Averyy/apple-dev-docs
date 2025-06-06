# cache(_:willEvictObject:)

**Framework**: Foundation  
**Kind**: method

Called when an object is about to be evicted or removed from the cache.

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
optional func cache(_ cache: NSCache<AnyObject, AnyObject>, willEvictObject obj: Any)
```

#### Discussion

It is not possible to modify `cache` from within the implementation of this delegate method.

## Parameters

- `cache`: The cache with which the object of interest is associated.
- `obj`: The object of interest in the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscachedelegate/cache(_:willevictobject:))*