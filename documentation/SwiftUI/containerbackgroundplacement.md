# ContainerBackgroundPlacement

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

This method controls where to place a background that you specify with the [`containerBackground(_:for:)`](./view/containerbackground%28_,for%29.md) or [`containerBackground(for:alignment:content:)`](./view/containerbackground%28for,alignment,content%29.md) modifier.

## Topics

### Getting placements
- [static let navigation: ContainerBackgroundPlacement](./containerbackgroundplacement/navigation.md)
  A background placement inside a [`NavigationStack`](./navigationstack.md) or [`NavigationSplitView`](./navigationsplitview.md).
- [static let tabView: ContainerBackgroundPlacement](./containerbackgroundplacement/tabview.md)
  A background placement inside a [`TabView`](./tabview.md).
- [static let widget: ContainerBackgroundPlacement](./containerbackgroundplacement/widget.md)
  The container background placement for a widget.
### Getting StoreKit placements
- [static var subscriptionStore: ContainerBackgroundPlacement](./containerbackgroundplacement/subscriptionstore.md)
  An automatic placement within a subscription store view, based on the view’s context.
- [static var subscriptionStoreFullHeight: ContainerBackgroundPlacement](./containerbackgroundplacement/subscriptionstorefullheight.md)
  A background placement that spans the full height of a subscription store view.
- [static var subscriptionStoreHeader: ContainerBackgroundPlacement](./containerbackgroundplacement/subscriptionstoreheader.md)
  A background placement behind the marketing content of a subscription store view.
### Type Properties
- [static let navigationSplitView: ContainerBackgroundPlacement](./containerbackgroundplacement/navigationsplitview.md)
  A background placement behind the content of a [`NavigationSplitView`](./navigationsplitview.md).
- [static let window: ContainerBackgroundPlacement](./containerbackgroundplacement/window.md)
  A  background placement inside a [`Window`](./window.md) or [`WindowGroup`](./windowgroup.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Layering views
- [Adding a background to your view](./adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
- [struct ZStack](./zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](./view/zindex%28_%29.md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](./view/background%28alignment,content%29.md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./view/background%28_,ignoressafeareaedges%29.md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](./view/background%28ignoressafeareaedges%29.md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](./view/background%28_,in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](./view/background%28in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](./view/overlay%28alignment,content%29.md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./view/overlay%28_,ignoressafeareaedges%29.md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](./view/overlay%28_,in,fillstyle%29.md)
  Layers a shape that you specify in front of this view.
- [var backgroundMaterial: Material?](./environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](./view/containerbackground%28_,for%29.md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](./view/containerbackground%28for,alignment,content%29.md)
  Sets the container background of the enclosing container using a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/containerbackgroundplacement)*