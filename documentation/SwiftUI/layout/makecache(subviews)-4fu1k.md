# makeCache(subviews:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns the empty value when your layout doesn’t require a cache.

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
func makeCache(subviews: Self.Subviews) -> Self.Cache
```

Available when `Cache` is `()`.

## Discussion

If you don’t implement the [`makeCache(subviews:)`](./makecache%28subviews%29-4fu1k.md) method in your custom layout, the protocol uses this default implementation instead, which returns an empty value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/makecache(subviews:)-4fu1k)*