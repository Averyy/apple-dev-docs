# init(primary:secondary:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an arrangement view with a primary and secondary view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
nonisolated
init(@ContentBuilder primary: () -> Primary, @ContentBuilder secondary: () -> Secondary)
```

## Discussion

Use this initializer to create an arrangement view that lays out two pieces of content. The arrangement view adapts the layout of the primary and secondary views based on the context, including size class and hardware features.

By default, the arrangement view uses an automatic style, which resolves to a split arrangement. Use the [`arrangementViewStyle(_:)`](../view/arrangementviewstyle%28_%29.md) modifier to specify how the views are arranged:

```swift
ArrangementView {
    PhotosView()
} secondary: {
    PhotosDetailPanelView()
}
.arrangementViewStyle(.split)
```

## Parameters

- `primary`: The view to display as the primary content in the arrangement.
- `secondary`: The view to display as the secondary content in the arrangement.

## See Also

### Creating an arrangement view
- [init(ArrangementViewStyleConfiguration)](./init%28_%29.md)
  Creates an arrangement view from a style configuration.
- [struct ArrangementViewStyleConfiguration](../arrangementviewstyleconfiguration.md)
  The properties of an arrangement view you provide to create a custom style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementview/init(primary:secondary:))*