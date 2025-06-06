# ToolbarTitleDisplayMode

**Framework**: SwiftUI  
**Kind**: struct

A type that defines the behavior of title of a toolbar.

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
struct ToolbarTitleDisplayMode
```

#### Overview

Use the [`toolbarTitleDisplayMode(_:)`](view/toolbartitledisplaymode(_:).md) modifier to configure the title display behavior of your toolbar:

```swift
NavigationStack {
    ContentView()
        .toolbarTitleDisplayMode(.inlineLarge)
}
```

## Topics

### Getting display modes
- [static var automatic: ToolbarTitleDisplayMode](toolbartitledisplaymode/automatic.md)
  The automatic mode.
- [static var inline: ToolbarTitleDisplayMode](toolbartitledisplaymode/inline.md)
  The inline mode.
- [static var inlineLarge: ToolbarTitleDisplayMode](toolbartitledisplaymode/inlinelarge.md)
  The inline large mode.
- [static var large: ToolbarTitleDisplayMode](toolbartitledisplaymode/large.md)
  The large mode.

## See Also

- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](view/toolbartitledisplaymode(_:).md)
  Configures the toolbar title display mode for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbartitledisplaymode)*