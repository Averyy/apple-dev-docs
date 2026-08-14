# NIDLTDOAConfiguration.DiscoveryMethod

**Framework**: Nearby Interaction  
**Kind**: enum

The technologies an app can use to discover Downlink Time-Difference-of-Arrival anchors.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum DiscoveryMethod
```

#### Overview

When you create a DL-TDOA configuration ([`NIDLTDOAConfiguration`](nidltdoaconfiguration.md)), specify the method that the session uses to discover nearby anchors, among Wi-Fi or Bluetooth Low Energy, by calling [`init(networkIdentifier:discoveryMethod:)`](nidltdoaconfiguration/init(networkidentifier:discoverymethod:).md). The framework needs to know the anchor discovery technology upfront, to match your deployment environment.

The default value is [`NIDLTDOAConfiguration.DiscoveryMethod.bluetoothLowEnergy`](nidltdoaconfiguration/discoverymethod-swift.enum/bluetoothlowenergy.md).

## Topics

### Specifying the discovery technology
- [NIDLTDOAConfiguration.DiscoveryMethod.wifi](nidltdoaconfiguration/discoverymethod-swift.enum/wifi.md)
  A method to discover DL-TDOA anchors using Wi-Fi.
- [NIDLTDOAConfiguration.DiscoveryMethod.bluetoothLowEnergy](nidltdoaconfiguration/discoverymethod-swift.enum/bluetoothlowenergy.md)
  A method to discover DL-TDOA anchors using Bluetooth Low Energy.
### Createing a discovery method
- [init?(rawValue: Int)](nidltdoaconfiguration/discoverymethod-swift.enum/init(rawvalue:).md)
  Initializes a discovery method from a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var discoveryMethod: NIDLTDOAConfiguration.DiscoveryMethod](nidltdoaconfiguration/discoverymethod-swift.property.md)
  The technology your app uses to discover DL-TDOA anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoaconfiguration/discoverymethod-swift.enum)*