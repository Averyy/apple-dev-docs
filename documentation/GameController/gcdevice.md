# GCDevice

**Framework**: Game Controller  
**Kind**: protocol

A protocol that defines a common interface for game input devices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCDevice : NSObjectProtocol
```

#### Overview

This protocol provides common properties for game controllers, and mouse and keyboard devices.

## Topics

### Getting device information
- [var vendorName: String?](gcdevice/vendorname.md)
  The manufacturer-provided name for the device, or the user’s name for the device.
- [var productCategory: String](gcdevice/productcategory.md)
  The product category that identifies the type of controller.
- [Product category constants](product-category-constants.md)
### Handling input
- [var handlerQueue: dispatch_queue_t](gcdevice/handlerqueue.md)
  The dispatch queue that the framework uses to call element value change handlers.
- [var physicalInputProfile: GCPhysicalInputProfile](gcdevice/physicalinputprofile.md)
  The device’s physical input profile, such as a controller’s extended gamepad.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [GCController](gccontroller.md)
- [GCKeyboard](gckeyboard.md)
- [GCMouse](gcmouse.md)
- [GCRacingWheel](gcracingwheel.md)

## See Also

- [Supporting Game Controllers](supporting-game-controllers.md)
  Support a physical controller or add a virtual controller to enhance how people interact with your game through haptics, lighting, and motion sensing.
- [Letting players use their second-generation Siri Remote as a game controller](letting-players-use-their-second-generation-siri-remote-as-a-game-controller.md)
  Support the second-generation Siri Remote as a game controller in your Apple TV game.
- [class GCController](gccontroller.md)
  A representation of a real game controller, a virtual controller, or a snapshot of a controller.
- [class GCRacingWheel](gcracingwheel.md)
  An object that represents a physical racing wheel controller connected to a device.
- [class GCKeyboard](gckeyboard.md)
  An object that represents a physical keyboard connected to a device.
- [class GCMouse](gcmouse.md)
  An object that represents a physical mouse connected to a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevice)*