# cameraStreamControl(_:didStopStreamWithError:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that the camera stream has stopped.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func cameraStreamControl(_ cameraStreamControl: HMCameraStreamControl, didStopStreamWithError error: (any Error)?)
```

## Parameters

- `cameraStreamControl`: The stream control responsible for the camera stream.
- `error`: If the stream stops because of an error, this is an error object with details;   otherwise.

## See Also

- [func cameraStreamControlDidStartStream(HMCameraStreamControl)](hmcamerastreamcontroldelegate/camerastreamcontroldidstartstream(_:).md)
  Tells the delegate that the camera stream has started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamcontroldelegate/camerastreamcontrol(_:didstopstreamwitherror:))*