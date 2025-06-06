# CBCentralManager.Feature

**Framework**: Core Bluetooth  
**Kind**: struct

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

## Topics

### Creating a Central Manager Feature Instance
- [init(rawValue: UInt)](cbcentralmanager/feature/init(rawvalue:).md)
  Creates a central manager feature instance.
### Extended Scan Features
- [static var extendedScanAndConnect: CBCentralManager.Feature](cbcentralmanager/feature/extendedscanandconnect.md)
  The hardware supports extended scans and enhanced connection creation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func supports(CBCentralManager.Feature) -> Bool](cbcentralmanager/supports(_:).md)
  Returns a Boolean that indicates whether the device supports a specific set of features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/feature)*