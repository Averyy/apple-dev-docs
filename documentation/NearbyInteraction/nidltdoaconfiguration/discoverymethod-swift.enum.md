# NIDLTDOAConfiguration.DiscoveryMethod

**Framework**: Nearby Interaction  
**Kind**: enum  
**Role**: Enumeration

The technologies an app can use to discover Downlink Time-Difference-of-Arrival anchors.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum DiscoveryMethod
```

```c
enum NIDLTDOADiscoveryMethod : NSInteger;
```

## Overview

When you create a DL-TDOA configuration ([`NIDLTDOAConfiguration`](../nidltdoaconfiguration.md)), specify the method that the session uses to discover nearby anchors, among Wi-Fi or Bluetooth Low Energy, by calling [`init(networkIdentifier:discoveryMethod:)`](./init%28networkidentifier,discoverymethod%29.md). The framework needs to know the anchor discovery technology upfront, to match your deployment environment.

The default value is [`NIDLTDOAConfiguration.DiscoveryMethod.bluetoothLowEnergy`](./discoverymethod-swift.enum/bluetoothlowenergy.md).

## Topics

### Specifying the discovery technology
- [NIDLTDOAConfiguration.DiscoveryMethod.wifi](./discoverymethod-swift.enum/wifi.md)
  A method to discover DL-TDOA anchors using Wi-Fi.
- [NIDLTDOAConfiguration.DiscoveryMethod.bluetoothLowEnergy](./discoverymethod-swift.enum/bluetoothlowenergy.md)
  A method to discover DL-TDOA anchors using Bluetooth Low Energy.
### Createing a discovery method
- [init?(rawValue: Int)](./discoverymethod-swift.enum/init%28rawvalue%29.md)
  Initializes a discovery method from a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifing the discovery method
- [var discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod](./discoverymethod-swift.property.md)
  The technology your app uses to discover DL-TDOA anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration/discoverymethod-swift.enum)*