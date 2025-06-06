# nextDrawable()

**Framework**: Core Animation  
**Kind**: method

Waits until a Metal drawable is available, and then returns it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func nextDrawable() -> (any CAMetalDrawable)?
```

#### Return Value

A Metal drawable. Use the drawable’s [`texture`](cametaldrawable/texture.md) property to configure a [`MTLRenderPipelineColorAttachmentDescriptor`](https://developer.apple.com/documentation/Metal/MTLRenderPipelineColorAttachmentDescriptor) object for rendering to the layer.

#### Discussion

A [`CAMetalLayer`](cametallayer.md) object maintains an internal pool of textures for displaying layer content, each wrapped in a [`CAMetalDrawable`](cametaldrawable.md) object. Use this method to retrieve the next available drawable from the pool. If all drawables are in use, the layer waits up to one second for one to become available, after which it returns `nil`. The [`allowsNextDrawableTimeout`](cametallayer/allowsnextdrawabletimeout.md) property affects this behavior.

This method returns `nil` if the layer’s [`pixelFormat`](cametallayer/pixelformat.md) or other properties are invalid.

## See Also

- [var maximumDrawableCount: Int](cametallayer/maximumdrawablecount.md)
  The number of Metal drawables in the resource pool managed by Core Animation.
- [var allowsNextDrawableTimeout: Bool](cametallayer/allowsnextdrawabletimeout.md)
  A Boolean value that determines whether requests for a new buffer expire if the system can’t satisfy them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/nextdrawable())*