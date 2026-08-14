# CMWaterSubmersionEvent

**Framework**: Core Motion  
**Kind**: class

An event indicating that the device’s submersion state has changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CMWaterSubmersionEvent
```

## Topics

### Accessing event data
- [var date: Date](cmwatersubmersionevent/date.md)
  The time and date of the event.
- [var state: CMWaterSubmersionEvent.State](cmwatersubmersionevent/state-swift.property.md)
  The new submersion state.
- [CMWaterSubmersionEvent.State](cmwatersubmersionevent/state-swift.enum.md)
  The device’s submersion state.
### Initializers
- [init?(coder: NSCoder)](cmwatersubmersionevent/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Accessing submersion data](accessing-submersion-data.md)
  Use a water-submersion manager to receive water pressure, temperature, and depth data on Apple Watch Ultra.
- [class CMWaterSubmersionManager](cmwatersubmersionmanager.md)
  An object for managing the collection of pressure and temperature data during submersion.
- [protocol CMWaterSubmersionManagerDelegate](cmwatersubmersionmanagerdelegate.md)
  A delegate that receives updates about ambient pressure, water pressure, water temperature, and submersion events.
- [class CMWaterSubmersionMeasurement](cmwatersubmersionmeasurement.md)
  An update that contains data about the pressure and depth.
- [class CMWaterTemperature](cmwatertemperature.md)
  An update that contains data about the water temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)*