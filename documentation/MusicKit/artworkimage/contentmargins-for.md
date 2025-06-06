# contentMargins(_:for:)

**Framework**: MusicKit  
**Kind**: method

Configures the content margin for a provided placement.

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
func contentMargins(_ length: CGFloat, for placement: ContentMarginPlacement = .automatic) -> some View
```

#### Discussion

Use this modifier to customize the content margins of different kinds of views. For example, you can use this modifier to customize the margins of scrollable views like `ScrollView`. In the following example, the scroll view will automatically inset its content by the safe area plus an additional 20 points on the leading and trailing edge.

```swift
ScrollView(.horizontal) {
    // ...
}
.contentMargins(.horizontal, 20.0)
```

You can provide a `ContentMarginPlacement` to target specific parts of a view to customize. For example, provide a `ContentMargingPlacement/scrollContent` placement to inset the content of a `TextEditor` without affecting the insets of its scroll indicators.

```swift
TextEditor(text: $text)
    .contentMargins(.horizontal, 20.0, for: .scrollContent)
```

Similarly, you can customize the insets of scroll indicators separately from scroll content. Consider doing this when applying a custom clip shape that may clip the indicators.

```swift
ScrollView {
    // ...
}
.clipShape(.rect(cornerRadius: 20.0))
.contentMargins(10.0, for: .scrollIndicators)
```

When applying multiple contentMargins modifiers, modifiers with the same placement will override modifiers higher up in the view hierarchy.

## Parameters

- `length`: The amount of margins to add on all edges.
- `placement`: Where the margins should be added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/contentmargins(_:for:))*