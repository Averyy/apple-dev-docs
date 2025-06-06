# safeAreaPadding(_:_:)

**Framework**: SwiftUI  
**Kind**: method

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
nonisolated
func safeAreaPadding(_ edges: Edge.Set = .all, _ length: CGFloat? = nil) -> some View
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

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for adding to the safe area based on the size of a view.

## See Also

- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](view/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func safeAreaInset(edge:alignment:spacing:content:)](view/safeareainset(edge:alignment:spacing:content:).md)
  Shows the specified content beside the modified view.
- [func safeAreaPadding(_:)](view/safeareapadding(_:).md)
  Adds the provided insets into the safe area of this view.
- [struct SafeAreaRegions](safearearegions.md)
  A set of symbolic safe area regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/safeareapadding(_:_:))*