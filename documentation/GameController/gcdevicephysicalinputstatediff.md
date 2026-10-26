# GCDevicePhysicalInputStateDiff

**Framework**: Game Controller  
**Kind**: protocol  
**Role**: Protocol

The common functions for objects that contain the differences between a current and previous input state object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCDevicePhysicalInputStateDiff : NSObjectProtocol
```

```objc
@protocol GCDevicePhysicalInputStateDiff <NSObject>
```

#### Overview

Use the `GCDevicePhysicalInput` [`nextInputState()`](./gcdevicephysicalinput/nextinputstate%28%29.md) method to get an input state object conforming to this protocol.

## Topics

### Getting changes
- [func change(for: any GCPhysicalInputElement) -> GCDevicePhysicalInputElementChange](./gcdevicephysicalinputstatediff/change%28for%29.md)
  Returns whether the input value of an element changes.
- [enum GCDevicePhysicalInputElementChange](./gcdevicephysicalinputelementchange.md)
  Possible values that describe whether the input value of an element changes.
- [func changedElements() -> NSEnumerator?](./gcdevicephysicalinputstatediff/changedelements%28%29-9cdq4.md)
  Returns the elements that changed since the previous input state.
- [func changedElements() -> (some Sequence<any GCPhysicalInputElement>)?
](./gcdevicephysicalinputstatediff/changedelements%28%29-2zzwm.md)
  Returns the elements that changed since the previous input state.
- [- changedElements](./gcdevicephysicalinputstatediff/changedelements.md)
  Returns the elements that changed since the previous input state.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Essentials
- [Handling input events](./handling-input-events.md)
  Receive controller input using either polling or callbacks.
- [protocol GCDevicePhysicalInput](./gcdevicephysicalinput.md)
  The common properties and methods for objects that represent the input profile of a device.
- [protocol GCDevicePhysicalInputState](./gcdevicephysicalinputstate.md)
  The common properties for physical devices with elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicephysicalinputstatediff)*