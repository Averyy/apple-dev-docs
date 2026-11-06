# toolbarTitleDisplayMode(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the toolbar title display mode for this view.

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
func toolbarTitleDisplayMode(_ mode: ToolbarTitleDisplayMode) -> some View
```

## Discussion

Use this modifier to override the default toolbar title display mode.

```swift
NavigationStack {
    ContentView()
        .toolbarTitleDisplayMode(.inlineLarge)
}
```

See [`ToolbarTitleDisplayMode`](../toolbartitledisplaymode.md) for more information on the different kinds of display modes. This modifier has no effect on macOS.

## See Also

### Configuring the toolbar title display
- [struct ToolbarTitleDisplayMode](../toolbartitledisplaymode.md)
  A type that defines the behavior of title of a toolbar.
- [func toolbarTitleAlignment(ToolbarTitleAlignment) -> some View](./toolbartitlealignment%28_%29.md)
  Sets the preferred alignment of the navigation bar’s title.
- [struct ToolbarTitleAlignment](../toolbartitlealignment.md)
  A preferred alignment for a navigation bar’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbartitledisplaymode(_:))*