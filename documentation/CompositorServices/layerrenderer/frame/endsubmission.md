# endSubmission()

**Framework**: Compositor Services  
**Kind**: method

Notifies Compositor Services that you finished generating the GPU commands to render the specified frame.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func endSubmission()
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

This function helps you optimize your app’s rendering efficiency. Call [`startSubmission()`](layerrenderer/frame/startsubmission().md) function before you start any of the GPU work that depends on the device pose. Call this function after you build your Metal command buffers and are ready to commit the frame to the GPU. Compositor Services uses the time difference to improve its predictions for when to start the frame submission process. Those predictions help you schedule the encoding process at a more optimal time for the system.

## See Also

- [func startSubmission()](layerrenderer/frame/startsubmission.md)
  Notifies Compositor Services that you’re ready to generate the Metal commands to render the specified frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/endsubmission())*