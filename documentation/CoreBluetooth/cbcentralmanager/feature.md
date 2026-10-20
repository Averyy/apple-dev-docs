# CBCentralManager.Feature

**Framework**: Core Bluetooth  
**Kind**: struct  
**Role**: Structure

An option set of device-specific features.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct Feature
```

```c
enum CBCentralManagerFeature : NSUInteger;
```

## Topics

### Creating a Central Manager Feature Instance
- [init(rawValue: UInt)](./feature/init%28rawvalue%29.md)
  Creates a central manager feature instance.
### Extended Scan Features
- [static var extendedScanAndConnect: CBCentralManager.Feature](./feature/extendedscanandconnect.md)
  The hardware supports extended scans and enhanced connection creation.
### Type Properties
- [static var channelSounding: CBCentralManager.Feature](./feature/channelsounding.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Inspecting Feature Support
- [class func supports(CBCentralManager.Feature) -> Bool](./supports%28_%29.md)
  Returns a Boolean that indicates whether the device supports a specific set of features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/feature)*