# explicitAlignment(of:in:proposal:subviews:cache:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns the result of merging the horizontal alignment guides of all subviews.

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
func explicitAlignment(of guide: HorizontalAlignment, in bounds: CGRect, proposal: ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) -> CGFloat?
```

#### Discussion

If you don’t implement the [`explicitAlignment(of:in:proposal:subviews:cache:)`](./explicitalignment%28of,in,proposal,subviews,cache%29-8cl0p.md) method in your custom layout, the protocol uses this default implementation instead, which merges the guides of all the subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/explicitalignment(of:in:proposal:subviews:cache:)-8cl0p)*