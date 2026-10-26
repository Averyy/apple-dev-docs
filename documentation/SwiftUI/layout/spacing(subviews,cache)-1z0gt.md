# spacing(subviews:cache:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns the union of all subview spacing.

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
func spacing(subviews: Self.Subviews, cache: inout Self.Cache) -> ViewSpacing
```

#### Discussion

If you don’t implement the [`spacing(subviews:cache:)`](./spacing%28subviews,cache%29-1z0gt.md) method in your custom layout, the protocol uses this default implementation instead, which returns the union of the spacing preferences of all the layout’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/spacing(subviews:cache:)-1z0gt)*