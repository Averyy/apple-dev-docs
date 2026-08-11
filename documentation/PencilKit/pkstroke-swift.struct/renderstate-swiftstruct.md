# PKStroke.RenderState

**Framework**: PencilKit  
**Kind**: struct

A value that captures the render-time state of a stroke, such as grain texture position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RenderState
```

## Mentions

- [Controlling stroke rendering for animation and editing](controlling-stroke-rendering-for-animation-and-editing.md)

#### Overview

Use `RenderState` to preserve rendering fidelity when you manipulate strokes programmatically. For example, substrokes returned by [`substroke(range:)`](pkstroke-swift.struct/substroke(range:).md) may include a `renderState` so that the extracted portion renders identically to the corresponding section of the original stroke. A value of `nil` uses default rendering.

The [`grainOffset`](pkstroke-swift.struct/renderstate-swift.struct/grainoffset.md) property is directly readable and writable. All state, including opaque internal properties, can be persisted by encoding the value using `Codable`.

## Topics

### Creating a render state
- [init(grainOffset: CGPoint?)](pkstroke-swift.struct/renderstate-swift.struct/init(grainoffset:).md)
  Creates a render state with the specified grain offset.
### Getting the render state
- [var grainOffset: CGPoint?](pkstroke-swift.struct/renderstate-swift.struct/grainoffset.md)
  The pre-transform position of the grain texture for strokes with a backing grain texture such as crayon.
### Using reference types
- [class PKStrokeRenderStateReference](pkstrokerenderstatereference.md)
  An object that captures the render-time state of a stroke, such as grain texture position.
### Initializers
- [init(PKStrokeRenderStateReference)](pkstroke-swift.struct/renderstate-swift.struct/init(_:).md)
  Creates a `RenderState` from its Objective-C counterpart `PKStrokeRenderStateReference`.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var renderGroupID: UUID?](pkstroke-swift.struct/rendergroupid.md)
  Strokes with certain inks (such as marker) can composite to look as if they were drawn while the previous stroke with the same ink was still wet. This UUID may be set to a single value for a run of strokes which should be rendered together in this manner.
- [var renderState: PKStroke.RenderState?](pkstroke-swift.struct/renderstate-swift.property.md)
  Contains information about the render details (such as particle positioning) of this stroke, which can be useful when manipulating the model in certain ways. For example, this may be set on substrokes returned by `substroke(range:)`. nil uses default rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/renderstate-swift.struct)*