# cameraStreamControl(_:didStopStreamWithError:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cameraStreamControl:(HMCameraStreamControl *) cameraStreamControl didStopStreamWithError:(NSError *) error;
```

## Parameters

- `cameraStreamControl`: The stream control responsible for the camera stream.
- `error`: If the stream stops because of an error, this is an error object with details; `nil` otherwise.

## See Also

### Observing stream activity
- [func cameraStreamControlDidStartStream(HMCameraStreamControl)](./camerastreamcontroldidstartstream%28_%29.md)
  Tells the delegate that the camera stream has started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamcontroldelegate/camerastreamcontrol(_:didstopstreamwitherror:))*