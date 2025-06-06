# labelStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for labels within this view.

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
func labelStyle<S>(_ style: S) -> some View where S : LabelStyle
```

#### Discussion

Use this modifier to set a specific style for all labels within a view:

```swift
VStack {
    Label("Fire", systemImage: "flame.fill")
    Label("Lightning", systemImage: "bolt.fill")
}
.labelStyle(MyCustomLabelStyle())
```

## See Also

- [struct Text](text.md)
  A view that displays one or more lines of read-only text.
- [struct Label](label.md)
  A standard label for user interface items, consisting of an icon with a title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/labelstyle(_:))*