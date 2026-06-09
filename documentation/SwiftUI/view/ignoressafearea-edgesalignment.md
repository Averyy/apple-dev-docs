# ignoresSafeArea(_:edges:alignment:)

**Framework**: SwiftUI  
**Kind**: method

Expands the safe area of a view aligning content within the new bounds using the provided alignment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func ignoresSafeArea(_ regions: SafeAreaRegions = .all, edges: Edge.Set = .all, alignment: Alignment?) -> some View
```

#### Return Value

A view with an expanded safe area.

#### Discussion

By default, the SwiftUI layout system sizes and positions views to avoid certain safe areas. This ensures that system content like the software keyboard or edges of the device don’t obstruct your views. To extend your content into these regions, you can ignore safe areas on specific edges by applying this modifier.

When expanding the safe area, the SwiftUI layout system proposes the expanded size to the view. If your view has a fixed size, you can use the alignment property to determine how the fixed size view should be aligned in the expanded bounds.

For examples of how to use this modifier, see [`Adding a background to your view`](adding-a-background-to-your-view.md).

## Parameters

- `regions`: The regions to expand the view’s safe area into. The modifier expands into all safe area region types by default.
- `edges`: The set of edges to expand. Any edges that you don’t include in this set remain unchanged. The set includes all edges by default.
- `alignment`: The alignment of this view inside the resulting frame. Note that most alignment values have no apparent effect when the size of the frame happens to match that of this view.

## See Also

- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](view/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func safeAreaInset(edge:alignment:spacing:content:)](view/safeareainset(edge:alignment:spacing:content:).md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(_:)](view/safeareapadding(_:).md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](view/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.
- [struct SafeAreaRegions](safearearegions.md)
  A set of symbolic safe area regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ignoressafearea(_:edges:alignment:))*