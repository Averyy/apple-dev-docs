# safeAreaPadding(_:)

**Framework**: FamilyControls  
**Kind**: method

Adds the provided insets into the safe area of this view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func safeAreaPadding(_ length: CGFloat) -> some View
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/safeareapadding(_:)-5mlax)*