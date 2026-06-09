# renderGroupID

**Framework**: PencilKit  
**Kind**: property

Strokes with certain inks (such as marker) can composite to look as if they were drawn while the previous stroke with the same ink was still wet. This UUID may be set to a single value for a run of strokes which should be rendered together in this manner.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var renderGroupID: UUID? { get set }
```

## Mentions

- [Controlling stroke rendering for animation and editing](controlling-stroke-rendering-for-animation-and-editing.md)

## See Also

- [var renderState: PKStroke.RenderState?](pkstroke-swift.struct/renderstate-swift.property.md)
  Contains information about the render details (such as particle positioning) of this stroke, which can be useful when manipulating the model in certain ways. For example, this may be set on substrokes returned by `substroke(range:)`. nil uses default rendering.
- [PKStroke.RenderState](pkstroke-swift.struct/renderstate-swift.struct.md)
  A value that captures the render-time state of a stroke, such as grain texture position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/rendergroupid)*