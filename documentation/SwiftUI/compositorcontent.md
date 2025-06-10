# CompositorContent

**Framework**: SwiftUI  
**Kind**: protocol

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
protocol CompositorContent
```

## Topics

### Associated Types
- [associatedtype Body : CompositorContent](compositorcontent/body-swift.associatedtype.md)
### Instance Properties
- [var body: Self.Body](compositorcontent/body-swift.property.md)
### Instance Methods
- [func contentCaptureProtected(Bool) -> some CompositorContent](compositorcontent/contentcaptureprotected(_:).md)
  Marks the view as a view that activates content protection during scene capture events, such as screenshots, screen recordings, screensharing, etc.
- [func onAppear(perform: (() -> Void)?) -> some CompositorContent](compositorcontent/onappear(perform:).md)
  Adds an action to perform before this content appears.
- [func onChange(of:initial:_:)](compositorcontent/onchange(of:initial:_:).md)
- [func onDisappear(perform: (() -> Void)?) -> some CompositorContent](compositorcontent/ondisappear(perform:).md)
  Adds an action to perform after this content disappears.
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some CompositorContent](compositorcontent/onimmersionchange(initial:_:).md)
  Performs an action when the immersion state of your app changes.
- [func onWorldRecenter(action:)](compositorcontent/onworldrecenter(action:).md)
  Adds an action to perform when recentering the view with the digital crown.
- [func persistentSystemOverlays(Visibility) -> some CompositorContent](compositorcontent/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func preferredSurroundingsEffect(SurroundingsEffect?) -> some CompositorContent](compositorcontent/preferredsurroundingseffect(_:).md)
  Applies an effect to passthrough video.
- [func upperLimbVisibility(Visibility) -> some CompositorContent](compositorcontent/upperlimbvisibility(_:).md)
  Sets the preferred visibility of the user’s upper limbs, while an [`ImmersiveSpace`](immersivespace.md) scene is presented.

## Relationships

### Conforming Types
- [CompositorContentBuilder.Content](compositorcontentbuilder/content.md)

## See Also

- [func blendMode(BlendMode) -> some View](view/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](view/compositinggroup.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](view/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [enum BlendMode](blendmode.md)
  Modes for compositing a view with overlapping content.
- [enum ColorRenderingMode](colorrenderingmode.md)
  The set of possible working color spaces for color-compositing operations.
- [struct CompositorContentBuilder](compositorcontentbuilder.md)
  A result builder for composing a collection of [`CompositorContent`](compositorcontent.md) elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontent)*