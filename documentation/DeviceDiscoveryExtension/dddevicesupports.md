# DDDeviceSupports

**Framework**: DeviceDiscoveryExtension  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
struct DDDeviceSupports
```

```c
enum DDDeviceSupports : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./dddevicesupports/init%28rawvalue%29.md)
### Type Properties
- [static var bluetoothHID: DDDeviceSupports](./dddevicesupports/bluetoothhid.md)
  Device supports bring up of classic transport profiles when low energy transport for peripheral is connected.
- [static var bluetoothPairingLE: DDDeviceSupports](./dddevicesupports/bluetoothpairingle.md)
- [static var bluetoothTransportBridging: DDDeviceSupports](./dddevicesupports/bluetoothtransportbridging.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevicesupports)*