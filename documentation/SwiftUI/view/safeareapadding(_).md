# safeAreaPadding(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds the provided insets into the safe area of this view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@export(implementation)
nonisolated func safeAreaPadding(_ insets: EdgeInsets) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func safeAreaPadding(_ length: CGFloat) -> some View
```

#### Discussion

Use this modifier when you would like to add a fixed amount of space to the safe area a view sees.

```swift
ScrollView(.horizontal) {
    HStack(spacing: 10.0) {
        ForEach(items) { item in
            ItemView(item)
        }
    }
}
.safeAreaPadding(.horizontal, 20.0)
```

See the horizontal [`safeAreaInset(edge:alignment:spacing:content:)`](./safeareainset%28edge,alignment,spacing,content%29-6gwby.md) or vertical [`safeAreaInset(edge:alignment:spacing:content:)`](./safeareainset%28edge,alignment,spacing,content%29-4s51l.md) modifier for adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](./ignoressafearea%28_,edges%29.md)
  Expands the safe area of a view.
- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set, alignment: Alignment?) -> some View](./ignoressafearea%28_,edges,alignment%29.md)
  Expands the safe area of a view aligning content within the new bounds using the provided alignment.
- [func safeAreaInset(edge:alignment:spacing:content:)](./safeareainset%28edge,alignment,spacing,content%29.md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](./safeareapadding%28_,_%29.md)
  Adds the provided insets into the safe area of this view.
- [struct SafeAreaRegions](../safearearegions.md)
  A set of symbolic safe area regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/safeareapadding(_:))*