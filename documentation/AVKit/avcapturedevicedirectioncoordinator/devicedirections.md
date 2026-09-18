# deviceDirections

**Framework**: AVKit  
**Kind**: property

The current direction of each camera the coordinator monitors, in relation to its view.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
var deviceDirections: AVCaptureDeviceDirectionMap { get }
```

## Mentions

- [Choosing a camera by the direction it faces](choosing-a-camera-by-the-direction-it-faces.md)

#### Discussion

The map groups the device types you passed at initialization by the direction they face. One array holds the devices that face the same direction as the view, and the other holds the devices that face away from it. Reading this property gives you the state at that moment. The change handler reports later changes.

> **Note**: This property is an empty [`AVCaptureDeviceDirectionMap`](avcapturedevicedirectionmap.md) until the coordinator calls its change handler for the first time. Treat that first callback, rather than initialization, as the point at which you know the directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedirectioncoordinator/devicedirections)*