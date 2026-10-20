# CompositorContent

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

A type that describes content a scene renders directly with Metal, rather than composing from SwiftUI views.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
protocol CompositorContent
```

#### Overview

Conform to this protocol when you draw an immersive scene with your own Metal renderer. Implement [`body`](./compositorcontent/body-swift.property.md) to describe the content, then pass the type to an [`ImmersiveSpace`](./immersivespace.md) in place of a view. The `CompositorLayer` type in CompositorServices gives you the render loop to draw into.

The following example wraps a renderer in a type that an immersive space can present:

```swift
struct StarField: CompositorContent {
    var body: some CompositorContent {
        CompositorLayer(configuration: StarFieldConfiguration()) {
            layerRenderer in
            renderLoop(layerRenderer)
        }
    }
}

@main
struct StarFieldApp: App {
    var body: some Scene {
        ImmersiveSpace {
            StarField()
        }
    }
}
```

Compose these types the same way you compose views: a body can contain another [`CompositorContent`](./compositorcontent.md), and [`AnyCompositorContent`](./anycompositorcontent.md) erases the concrete type when you need to return one of several kinds.

## Topics

### Associated Types
- [associatedtype Body : CompositorContent](./compositorcontent/body-swift.associatedtype.md)
### Instance Properties
- [var body: Self.Body](./compositorcontent/body-swift.property.md)
### Instance Methods
- [func contentCaptureProtected(Bool) -> some CompositorContent](./compositorcontent/contentcaptureprotected%28_%29.md)
  Marks the view as a view that activates content protection during scene capture events, such as screenshots, screen recordings, screensharing, etc.
- [func onAppear(perform: (() -> Void)?) -> some CompositorContent](./compositorcontent/onappear%28perform%29.md)
  Adds an action to perform before this content appears.
- [func onChange(of:initial:_:)](./compositorcontent/onchange%28of,initial,_%29.md)
- [func onDisappear(perform: (() -> Void)?) -> some CompositorContent](./compositorcontent/ondisappear%28perform%29.md)
  Adds an action to perform after this content disappears.
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some CompositorContent](./compositorcontent/onimmersionchange%28initial,_%29.md)
  Performs an action when the immersion state of your app changes.
- [func onWorldRecenter(action:)](./compositorcontent/onworldrecenter%28action%29.md)
  Adds an action to perform when recentering the view with the digital crown.
- [func persistentSystemOverlays(Visibility) -> some CompositorContent](./compositorcontent/persistentsystemoverlays%28_%29.md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some CompositorContent](./compositorcontent/preferredsurroundingseffect%28_%29.md)
  Applies an effect to passthrough video.
- [func upperLimbVisibility(Visibility) -> some CompositorContent](./compositorcontent/upperlimbvisibility%28_%29.md)
  Sets the preferred visibility of the user’s upper limbs, while an [`ImmersiveSpace`](./immersivespace.md) scene is presented.

## Relationships

### Conforming Types
- [AnyCompositorContent](./anycompositorcontent.md)
- [CompositorContentBuilder.Content](./compositorcontentbuilder/content.md)

## See Also

### Compositing views
- [func blendMode(BlendMode) -> some View](./view/blendmode%28_%29.md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](./view/compositinggroup%28%29.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](./view/drawinggroup%28opaque,colormode%29.md)
  Composites this view’s contents into an offscreen image before final display.
- [enum BlendMode](./blendmode.md)
  Modes for compositing a view with overlapping content.
- [enum ColorRenderingMode](./colorrenderingmode.md)
  The set of possible working color spaces for color-compositing operations.
- [struct CompositorContentBuilder](./compositorcontentbuilder.md)
  A result builder for composing a collection of [`CompositorContent`](./compositorcontent.md) elements.
- [struct AnyCompositorContent](./anycompositorcontent.md)
  Type erased compositor content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent)*