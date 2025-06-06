# CMWaterSubmersionEvent

**Framework**: Core Motion  
**Kind**: class

An event indicating that the device’s submersion state has changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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