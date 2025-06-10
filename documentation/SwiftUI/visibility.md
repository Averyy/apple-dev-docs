# Visibility

**Framework**: SwiftUI  
**Kind**: enum

The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
enum Visibility
```

#### Overview

For example, the preferred visibility of list row separators can be configured using the [`listRowSeparator(_:edges:)`](view/listrowseparator(_:edges:).md).

## Topics

### Getting visibility options
- [Visibility.automatic](visibility/automatic.md)
  The element may be visible or hidden depending on the policies of the component accepting the visibility configuration.
- [Visibility.visible](visibility/visible.md)
  The element may be visible.
- [Visibility.hidden](visibility/hidden.md)
  The element may be hidden.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func labelsHidden() -> some View](view/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](view/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [var labelsVisibility: Visibility](environmentvalues/labelsvisibility.md)
  The labels visibility set by [`labelsVisibility(_:)`](view/labelsvisibility(_:).md).
- [func menuIndicator(Visibility) -> some View](view/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func statusBarHidden(Bool) -> some View](view/statusbarhidden(_:).md)
  Sets the visibility of the status bar.
- [func persistentSystemOverlays(Visibility) -> some View](view/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visibility)*