# ToolbarTitleAlignment

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A preferred alignment for a navigation bar’s title.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
struct ToolbarTitleAlignment
```

## Overview

Use values of this type with the [`toolbarTitleAlignment(_:)`](./view/toolbartitlealignment%28_%29.md) modifier to override the title alignment the system would use.

```swift
NavigationStack {
    ContentView()
        .navigationTitle("Library")
        .toolbarTitleAlignment(.center)
}
```

To read the alignment the system actually used, see [`toolbarTitleAlignment`](./environmentvalues/toolbartitlealignment.md).

## Topics

### Getting title alignment options
- [static let automatic: ToolbarTitleAlignment](./toolbartitlealignment/automatic.md)
  The system determines the alignment.
- [static let center: ToolbarTitleAlignment](./toolbartitlealignment/center.md)
  The title is center-aligned.
- [static let leading: ToolbarTitleAlignment](./toolbartitlealignment/leading.md)
  The title is leading-aligned.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the toolbar title display
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](./view/toolbartitledisplaymode%28_%29.md)
  Configures the toolbar title display mode for this view.
- [struct ToolbarTitleDisplayMode](./toolbartitledisplaymode.md)
  A type that defines the behavior of title of a toolbar.
- [func toolbarTitleAlignment(ToolbarTitleAlignment) -> some View](./view/toolbartitlealignment%28_%29.md)
  Sets the preferred alignment of the navigation bar’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbartitlealignment)*