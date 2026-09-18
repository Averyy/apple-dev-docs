# init(view:deviceTypes:changeHandler:)

**Framework**: AVKit  
**Kind**: init

Creates a coordinator that reports the direction cameras face in relation to the specified view.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
init(view: UIView, deviceTypes: [AVCaptureDevice.DeviceType], changeHandler: ((AVCaptureDeviceDirectionMap) -> Void)? = nil)
```

#### Discussion

> **Note**: Initialize the coordinator only on the main actor.

## Parameters

- `view`: The view that camera directions are relative to.
- `deviceTypes`: The device types the coordinator considers. It reports no other cameras.
- `changeHandler`: A callback the coordinator invokes on the main actor soon after you create it, and again each time a camera changes direction. It receives an [`AVCaptureDeviceDirectionMap`](avcapturedevicedirectionmap.md) that groups the cameras by the direction they now face. Pass `nil` to read [`deviceDirections`](avcapturedevicedirectioncoordinator/devicedirections.md) yourself instead of receiving updates. A coordinator keeps the handler it’s created with, so create a new coordinator to change it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedirectioncoordinator/init(view:devicetypes:changehandler:))*