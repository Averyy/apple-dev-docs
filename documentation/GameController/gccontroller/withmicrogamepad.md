# withMicroGamepad()

**Framework**: Game Controller  
**Kind**: method

Returns a snapshot of a newly created controller with a micro gamepad profile.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func withMicroGamepad() -> GCController
```

#### Return Value

A snapshot with a micro gamepad profile.

#### Discussion

A snapshot is a copy of a real or virtual controller at a moment in time with its current element values. Unlike other controllers, you can set the values of a snapshot’s [`GCControllerElement`](gccontrollerelement.md) objects.

## See Also

- [class func withExtendedGamepad() -> GCController](gccontroller/withextendedgamepad.md)
  Returns a snapshot of a newly created controller with an extended gamepad profile.
- [func capture() -> GCController](gccontroller/capture.md)
  Returns a snapshot of the controller with its current element values.
- [var isSnapshot: Bool](gccontroller/issnapshot.md)
  A Boolean value that indicates whether the controller is a snapshot of a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/withmicrogamepad())*