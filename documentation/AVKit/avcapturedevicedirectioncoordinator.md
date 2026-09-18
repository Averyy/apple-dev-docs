# AVCaptureDeviceDirectionCoordinator

**Framework**: AVKit  
**Kind**: class

An object that tracks the direction each camera faces in relation to a view.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
class AVCaptureDeviceDirectionCoordinator
```

## Mentions

- [Choosing a camera by the direction it faces](choosing-a-camera-by-the-direction-it-faces.md)

#### Overview

A coordinator reports the direction each camera faces in relation to one view of your interface. It groups the cameras into the ones that face toward the person looking at that view, and the ones that face away. On a device with more than one display, a camera can change direction as the person opens, closes, or turns the device. The same camera captures that person in one configuration and the scene beyond the view in another. The [`position`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/position-swift.property) property is a fixed characteristic of the camera hardware, and it doesn’t change as the device does. Don’t read the direction a camera faces from it, because two cameras that report different positions can face the same way. Only a coordinator reports direction, and reports it again each time it changes.

Create a coordinator on the main actor, and pass the view that shows your preview and the device types your app captures from. The view is the coordinator’s frame of reference rather than something it draws into. Hold a strong reference to the coordinator for as long as that view stays onscreen.

Include your rear cameras alongside your front ones, because a rear camera can end up facing the person when they open or close the device, or when your view moves to a display that faces in the opposite direction.

> ❗ **Important**: If your app shows a preview on more than one display at once, create a coordinator for each view. Each reports direction in relation to its own view, so the same camera can be forward facing to one and backward facing to the other.

Read [`deviceDirections`](avcapturedevicedirectioncoordinator/devicedirections.md) for the direction of each camera at that moment, and pass a change handler to learn about later changes. The coordinator calls the handler on the main actor soon after you create it, then again on every change. In the following example, an observer creates a coordinator and hands each new forward-facing camera to the object that owns the capture session:

```swift
import AVKit

@MainActor
final class DirectionObserver {

    private var coordinator: AVCaptureDeviceDirectionCoordinator?

    func startObserving(previewView: UIView) {
        coordinator = AVCaptureDeviceDirectionCoordinator(
            view: previewView,
            deviceTypes: [.builtInOuterUltraWideCamera, .builtInInnerUltraWideCamera]
        ) { [weak self] deviceDirections in
            // Capture from the first camera that faces the person using the app.
            guard let descriptor = deviceDirections.forwardFacingDeviceDescriptors.first else { return }
            self?.selectCamera(with: descriptor)
        }
    }
}
```

The map names each camera with an [`AVCaptureDeviceDescriptor`](avcapturedevicedescriptor.md), which identifies a camera without being one. Pass the descriptor to the actor that owns your capture session, and create the [`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice) there, because configuring a capture device doesn’t belong on the main actor.

## Topics

### Creating a coordinator
- [init(view: UIView, deviceTypes: [AVCaptureDevice.DeviceType], changeHandler: ((AVCaptureDeviceDirectionMap) -> Void)?)](avcapturedevicedirectioncoordinator/init(view:devicetypes:changehandler:).md)
  Creates a coordinator that reports the direction cameras face in relation to the specified view.
### Reading the camera directions
- [var deviceDirections: AVCaptureDeviceDirectionMap](avcapturedevicedirectioncoordinator/devicedirections.md)
  The current direction of each camera the coordinator monitors, in relation to its view.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Choosing a camera by the direction it faces](choosing-a-camera-by-the-direction-it-faces.md)
  Find out which way each camera faces, and follow the change as someone opens and closes the device.
- [class AVCaptureDeviceDirectionMap](avcapturedevicedirectionmap.md)
  An object that groups the cameras a coordinator tracks by the direction they face.
- [class AVCaptureDeviceDescriptor](avcapturedevicedescriptor.md)
  An object that identifies a capture device and is safe to pass between actors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedirectioncoordinator)*