# withMicroGamepad()

**Framework**: Game Controller  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (GCController *) controllerWithMicroGamepad;
```

#### Return Value

A snapshot with a micro gamepad profile.

#### Discussion

A snapshot is a copy of a real or virtual controller at a moment in time with its current element values. Unlike other controllers, you can set the values of a snapshot’s [`GCControllerElement`](../gccontrollerelement.md) objects.

## See Also

### Creating snapshots
- [class func withExtendedGamepad() -> GCController](./withextendedgamepad%28%29.md)
  Returns a snapshot of a newly created controller with an extended gamepad profile.
- [func capture() -> GCController](./capture%28%29.md)
  Returns a snapshot of the controller with its current element values.
- [var isSnapshot: Bool](./issnapshot.md)
  A Boolean value that indicates whether the controller is a snapshot of a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/withmicrogamepad())*