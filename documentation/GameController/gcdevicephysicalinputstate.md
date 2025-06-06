# GCDevicePhysicalInputState

**Framework**: Game Controller  
**Kind**: protocol

The common properties for physical devices with elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCDevicePhysicalInputState : NSObjectProtocol
```

## Mentions

- [Handling input events](handling-input-events.md)

#### Overview

It’s safe to call any property and method implementation of this protocol from any thread, as long as you don’t do so from multiple threads concurrently.

## Topics

### Getting the device
- [var device: (any GCDevice)?](gcdevicephysicalinputstate/device.md)
  The physical device that this profile represents.
### Getting change information
- [var lastEventTimestamp: TimeInterval](gcdevicephysicalinputstate/lasteventtimestamp.md)
  The time of the most recent event.
- [var lastEventLatency: TimeInterval](gcdevicephysicalinputstate/lasteventlatency.md)
  The time in seconds between the last event and the current time.
### Accessing elements
- [var elements: GCPhysicalInputElementCollection<any GCPhysicalInputElement>](gcdevicephysicalinputstate/elements-46hgy.md)
  The device’s elements as key-value pairs for lookup by name.
- [var axes: GCPhysicalInputElementCollection<any GCAxisElement>](gcdevicephysicalinputstate/axes-5u1xr.md)
  The device’s axes as key-value pairs for lookup by name.
- [var buttons: GCPhysicalInputElementCollection<any GCButtonElement>](gcdevicephysicalinputstate/buttons-2ovae.md)
  The device’s buttons as key-value pairs for lookup by name.
- [var dpads: GCPhysicalInputElementCollection<any GCDirectionPadElement>](gcdevicephysicalinputstate/dpads-7b4o3.md)
  The device’s directional pads as key-value pairs for lookup by name.
- [var switches: GCPhysicalInputElementCollection<any GCSwitchElement>](gcdevicephysicalinputstate/switches-6dcny.md)
  The device’s switches as key-value pairs for lookup by name.
- [subscript(String) -> (any GCPhysicalInputElement)?](gcdevicephysicalinputstate/subscript(_:).md)
  Returns the element that the key specifies.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [GCDevicePhysicalInput](gcdevicephysicalinput.md)
### Conforming Types
- [GCControllerInputState](gccontrollerinputstate.md)
- [GCControllerLiveInput](gccontrollerliveinput.md)
- [GCRacingWheelInput](gcracingwheelinput.md)
- [GCRacingWheelInputState](gcracingwheelinputstate.md)

## See Also

- [Handling input events](handling-input-events.md)
  Receive controller input using either polling or callbacks.
- [protocol GCDevicePhysicalInput](gcdevicephysicalinput.md)
  The common properties and methods for objects that represent the input profile of a device.
- [protocol GCDevicePhysicalInputStateDiff](gcdevicephysicalinputstatediff.md)
  The common functions for objects that contain the differences between a current and previous input state object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstate)*