# ContainerBackgroundPlacement

**Framework**: SwiftUI  
**Kind**: struct

The placement of a container background.

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
struct ContainerBackgroundPlacement
```

#### Overview

This method controls where to place a background that you specify with the [`containerBackground(_:for:)`](view/containerbackground(_:for:).md) or [`containerBackground(for:alignment:content:)`](view/containerbackground(for:alignment:content:).md) modifier.

## Topics

### Getting placements
- [static let navigation: ContainerBackgroundPlacement](containerbackgroundplacement/navigation.md)
  A background placement inside a [`NavigationStack`](navigationstack.md) or [`NavigationSplitView`](navigationsplitview.md).
- [static let tabView: ContainerBackgroundPlacement](containerbackgroundplacement/tabview.md)
  A background placement inside a [`TabView`](tabview.md).
- [static let widget: ContainerBackgroundPlacement](containerbackgroundplacement/widget.md)
  The container background placement for a widget.
### Getting StoreKit placements
- [static var subscriptionStore: ContainerBackgroundPlacement](containerbackgroundplacement/subscriptionstore.md)
  An automatic placement within a subscription store view, based on the view’s context.
- [static var subscriptionStoreFullHeight: ContainerBackgroundPlacement](containerbackgroundplacement/subscriptionstorefullheight.md)
  A background placement that spans the full height of a subscription store view.
- [static var subscriptionStoreHeader: ContainerBackgroundPlacement](containerbackgroundplacement/subscriptionstoreheader.md)
  A background placement behind the marketing content of a subscription store view.
### Type Properties
- [static let navigationSplitView: ContainerBackgroundPlacement](containerbackgroundplacement/navigationsplitview.md)
  A background placement behind the content of a [`NavigationSplitView`](navigationsplitview.md).
- [static let window: ContainerBackgroundPlacement](containerbackgroundplacement/window.md)
  A  background placement inside a [`Window`](window.md) or [`WindowGroup`](windowgroup.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Adding a background to your view](adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
- [struct ZStack](zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](view/zindex(_:).md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](view/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](view/background(_:in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](view/background(in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](view/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](view/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [var backgroundMaterial: Material?](environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](view/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](view/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/containerbackgroundplacement)*