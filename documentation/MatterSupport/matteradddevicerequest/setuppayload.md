# setupPayload

**Framework**: MatterSupport  
**Kind**: property  
**Role**: Instance Property

The payload to use for Matter device setup.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
var setupPayload: MTRSetupPayload?
```

## Overview

This is an optional field for a setup to be able to complete. If this is provided, no QR-Code selection occurs. Use of this field requires an entitlement in the application ([com.apple.developer.matter.allow-setup-payload](../../BundleResources/entitlements/com.apple.developer.matter.allow-setup-payload.md)).

## See Also

### Setting up the request
- [MatterAddDeviceRequest.Home](./home.md)
  The representation of a home that appears in the picker during device setup.
- [MatterAddDeviceRequest.Room](./room.md)
  The representation of a room that appears in the picker during device setup.
- [MatterAddDeviceRequest.Topology](./topology-swift.struct.md)
  Information describing the properties of the ecosystem.
- [var topology: MatterAddDeviceRequest.Topology](./topology-swift.property.md)
  A configuration object representing the topology of the initiating ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/setuppayload)*