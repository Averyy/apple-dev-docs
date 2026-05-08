# Cache

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

Cached values associated with the layout instance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
associatedtype Cache = Void
```

#### Discussion

If you create a cache for your custom layout, you can use a type alias to define this type as your data storage type. Alternatively, you can refer to the data storage type directly in all the places where you work with the cache.

See [`makeCache(subviews:)`](layout/makecache(subviews:).md) for more information.

## See Also

- [func makeCache(subviews: Self.Subviews) -> Self.Cache](layout/makecache(subviews:).md)
  Creates and initializes a cache for a layout instance.
- [func updateCache(inout Self.Cache, subviews: Self.Subviews)](layout/updatecache(_:subviews:).md)
  Updates the layout’s cache when something changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/cache)*