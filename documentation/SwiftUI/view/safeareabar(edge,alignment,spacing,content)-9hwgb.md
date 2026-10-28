# safeAreaBar(edge:alignment:spacing:content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Shows the specified content as a custom bar above or below the modified view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func safeAreaBar(edge: VerticalEdge, alignment: HorizontalAlignment = .center, spacing: CGFloat? = nil, @ContentBuilder content: () -> some View) -> some View
```

**Other overloads**:

```swift
nonisolated
func safeAreaBar(edge: HorizontalEdge, alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ContentBuilder content: () -> some View) -> some View
```

## Return Value

A new view that displays `content` above or below the modified view, making space for the `content` view by vertically insetting the modified view, adjusting the safe area and scroll edge effects to match.

## Discussion

Similar to the [`safeAreaInset(edge:alignment:spacing:content:)`](./safeareainset%28edge,alignment,spacing,content%29-4s51l.md) modifier, the `content` view is anchored to the specified vertical edge of the parent view and its height insets the safe area.

Additionally, it extends the edge effect of any scroll views affected by the inset safe area.

## Parameters

- `edge`: The vertical edge of the view on which `content` is placed.
- `alignment`: The alignment guide used to position `content` horizontally.
- `spacing`: Extra distance placed between the two views, or nil to use the default amount of spacing.
- `content`: A content builder function providing the view to display as a custom bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:)-9hwgb)*