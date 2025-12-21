# encodePresent()

**Framework**: Compositor Services  
**Kind**: method

Encodes a notification event to the specified command buffer to present the drawable’s content onscreen.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func encodePresent()
```

#### Discussion

> **Note**: Commit the command buffer to the layer queue before calling present.

Call this function as the last step before committing the specified command buffer. Specifically, call it after you finish encoding all the work required to render the frame, and immediately before you call the command buffer’s [`commit()`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/commit()) method. The function adds a presentation event to the buffer that causes the compositor to display your frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/encodepresent())*