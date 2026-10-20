# ignoresSafeArea(_:edges:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Expands the safe area of a view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func ignoresSafeArea(_ regions: SafeAreaRegions = .all, edges: Edge.Set = .all) -> some View
```

## Mentions

- [Adding a background to your view](../adding-a-background-to-your-view.md)

#### Return Value

A view with an expanded safe area.

#### Discussion

By default, the SwiftUI layout system sizes and positions views to avoid certain safe areas. This ensures that system content like the software keyboard or edges of the device don’t obstruct your views. To extend your content into these regions, you can ignore safe areas on specific edges by applying this modifier.

When expanding the safe area, the SwiftUI layout system proposes the expanded size to the view. If your view has a fixed size, the alignment of the view may not be what you expect.

By default, SwiftUI resolves the alignment based on the edges being ignored. For example, providing only the bottom edge will result in a bottom alignment being used. You can use the `View/ignoresSafeArea(_:alignment:)` modifier to explicitly configure the alignment.

For examples of how to use this modifier, see [Adding a background to your view](../adding-a-background-to-your-view.md).

## Parameters

- `regions`: The regions to expand the view’s safe area into. The modifier expands into all safe area region types by default.
- `edges`: The set of edges to expand. Any edges that you don’t include in this set remain unchanged. The set includes all edges by default.

## See Also

### Staying in the safe areas
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set, alignment: Alignment?) -> some View](./ignoressafearea%28_,edges,alignment%29.md)
  Expands the safe area of a view aligning content within the new bounds using the provided alignment.
- [func safeAreaInset(edge:alignment:spacing:content:)](./safeareainset%28edge,alignment,spacing,content%29.md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(_:)](./safeareapadding%28_%29.md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](./safeareapadding%28_,_%29.md)
  Adds the provided insets into the safe area of this view.
- [struct SafeAreaRegions](../safearearegions.md)
  A set of symbolic safe area regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/ignoressafearea(_:edges:))*