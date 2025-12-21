# DevicePairingView

**Framework**: DeviceDiscoveryUI  
**Kind**: struct

A control that allows a user to become discoverable and advertise to local devices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
@preconcurrency struct DevicePairingView<Label, Fallback> where Label : View, Fallback : View
```

#### Overview

A `DevicePairingView` should be used to become discoverable to local devices from the user through a button interface.

## Topics

### Initializers
- [init(any ListenerProvider, access: DDDevicePairingAccess, label: () -> Label, fallback: () -> Fallback)](devicepairingview/init(_:access:label:fallback:).md)
  Creates a `DevicePairingView` which, when pressed, will display a local device advertiser interface.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryui/devicepairingview)*