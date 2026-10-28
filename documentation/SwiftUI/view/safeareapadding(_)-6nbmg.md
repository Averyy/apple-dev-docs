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
nonisolated func safeAreaPadding(_ length: CGFloat) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func safeAreaPadding(_ insets: EdgeInsets) -> some View
```

## Discussion

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/safeareapadding(_:)-6nbmg)*