# Visibility

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

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

For example, the preferred visibility of list row separators can be configured using the [`listRowSeparator(_:edges:)`](./view/listrowseparator%28_,edges%29.md).

## Topics

### Getting visibility options
- [Visibility.automatic](./visibility/automatic.md)
  The element may be visible or hidden depending on the policies of the component accepting the visibility configuration.
- [Visibility.visible](./visibility/visible.md)
  The element may be visible.
- [Visibility.hidden](./visibility/hidden.md)
  The element may be hidden.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CaseIterable](../Swift/caseiterable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Hiding system elements
- [func labelsHidden() -> some View](./view/labelshidden%28%29.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](./view/labelsvisibility%28_%29.md)
  Controls the visibility of labels of any controls contained within this view.
- [var labelsVisibility: Visibility](./environmentvalues/labelsvisibility.md)
  The labels visibility set by [`labelsVisibility(_:)`](./view/labelsvisibility%28_%29.md).
- [func menuIndicator(Visibility) -> some View](./view/menuindicator%28_%29.md)
  Sets the menu indicator visibility for controls within this view.
- [func persistentSystemOverlays(Visibility) -> some View](./view/persistentsystemoverlays%28_%29.md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func statusBarHidden(Bool) -> some View](./view/statusbarhidden%28_%29.md)
  Sets the visibility of the status bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visibility)*