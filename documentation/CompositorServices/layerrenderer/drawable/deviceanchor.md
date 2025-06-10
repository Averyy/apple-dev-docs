# deviceAnchor

**Framework**: Compositor Services  
**Kind**: property

The device position and orientation you used to render the frame.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var deviceAnchor: DeviceAnchor? { get nonmutating set }
```

#### Discussion

During rendering, match the camera position in your scene to the device anchor to create a better experience. In a visionOS app, the device anchor corresponds to the movements of someone’s head. If your camera movements aren’t synchronized to the device movements, the person might experience discomfort while viewing your content.

Because you encode your drawing commands before the final rendered frame appears, you must predict the device anchor in advance. ARKit provides the [`queryDeviceAnchor(atTimestamp:)`](https://developer.apple.com/documentation/ARKit/WorldTrackingProvider/queryDeviceAnchor(atTimestamp:)) function to help you determine this information. The value in the [`presentationTime`](layerrenderer/frame/timing/presentationtime.md) property represents the time for which you want the anchor. Start the prediction process at some point after the time specified by the [`optimalInputTime`](layerrenderer/frame/timing/optimalinputtime.md) property.

At display time, Compositor Services compares your predicted device anchor with the actual position and orientation of the device at that time. If the two values don’t match, Compositor Services adjusts the pixels of your frame to align it with the hardware. If you don’t want it to make this adjustment, set this property to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/deviceanchor)*