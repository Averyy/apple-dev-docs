# encodePresent()

**Framework**: Compositor Services  
**Kind**: method  
**Role**: Instance Method

Encodes a notification event to the specified command buffer to present the drawable’s content onscreen.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func encodePresent()
```

```c
void cp_drawable_mtl4_encode_present(cp_drawable_t drawable);
```

#### Discussion

> **Note**: Commit the command buffer to the layer queue before calling present.

Call this function as the last step before committing the specified command buffer. Specifically, call it after you finish encoding all the work required to render the frame, and immediately before you call the command buffer’s [`commit()`](../../../Metal/mtlcommandbuffer/commit%28%29.md) method. The function adds a presentation event to the buffer that causes the compositor to display your frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/encodepresent())*