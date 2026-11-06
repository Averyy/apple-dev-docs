# toolbarTitleAlignment(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the preferred alignment of the navigation bar’s title.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+

## Declaration

```swift
nonisolated
func toolbarTitleAlignment(_ alignment: ToolbarTitleAlignment) -> some View
```

## Discussion

The navigation bar resolves the alignment of its title automatically based on context, and toolbar roles. Use this modifier to override that resolution.

```swift
NavigationStack {
    ContentView()
        .navigationTitle("Library")
        .toolbarTitleAlignment(.center)
}
```

## Parameters

- `alignment`: The preferred navigation title alignment.

## See Also

### Configuring the toolbar title display
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](./toolbartitledisplaymode%28_%29.md)
  Configures the toolbar title display mode for this view.
- [struct ToolbarTitleDisplayMode](../toolbartitledisplaymode.md)
  A type that defines the behavior of title of a toolbar.
- [struct ToolbarTitleAlignment](../toolbartitlealignment.md)
  A preferred alignment for a navigation bar’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbartitlealignment(_:))*