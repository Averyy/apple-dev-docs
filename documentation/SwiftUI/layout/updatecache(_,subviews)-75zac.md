# updateCache(_:subviews:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Reinitializes a cache to a new value.

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
func updateCache(_ cache: inout Self.Cache, subviews: Self.Subviews)
```

## Discussion

If you don’t implement the [`updateCache(_:subviews:)`](./updatecache%28_,subviews%29-75zac.md) method in your custom layout, the protocol uses this default implementation instead, which calls [`makeCache(subviews:)`](./makecache%28subviews%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/updatecache(_:subviews:)-75zac)*