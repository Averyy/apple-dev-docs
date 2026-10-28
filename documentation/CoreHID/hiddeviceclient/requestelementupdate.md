# HIDDeviceClient.RequestElementUpdate

**Framework**: Core HID  
**Kind**: struct  
**Role**: Structure

A request to pull the current value from a list of HID elements

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct RequestElementUpdate
```

## Mentions

- [Communicating with human interface devices](../communicatingwithhiddevices.md)

## Overview

Provide this structure to [`updateElements(_:timeout:)`](./updateelements%28_,timeout%29.md) to request the current values for a list of elements. In most cases, this triggers a get report request to the device for all of the reports containing elements in the provided element list.

## Topics

### Initializers
- [init(elements: [HIDElement], pollDevice: Bool)](./requestelementupdate/init%28elements,polldevice%29.md)
  Creates a request element update.
### Instance Properties
- [var elements: [HIDElement]](./requestelementupdate/elements.md)
  The elements used to request updates.
- [var pollDevice: Bool](./requestelementupdate/polldevice.md)
  Whether the device should be polled for new updates.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [HIDElementUpdate](../hidelementupdate.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Update element values
- [func updateElements([any HIDElementUpdate], timeout: Duration?) async -> HIDDeviceClient.HIDElementUpdateResult](./updateelements%28_,timeout%29.md)
  Provide new update values for, or request current values from, lists of elements.
- [HIDDeviceClient.ProvideElementUpdate](./provideelementupdate.md)
  A structure that provides values for a list of HID elements.
- [HIDDeviceClient.HIDElementUpdateResult](./hidelementupdateresult.md)
  A class to hold the results of an element update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/requestelementupdate)*