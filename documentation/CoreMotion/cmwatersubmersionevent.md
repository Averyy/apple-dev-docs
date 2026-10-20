# CMWaterSubmersionEvent

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

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

```objc
@interface CMWaterSubmersionEvent : NSObject
```

## Topics

### Accessing event data
- [var date: Date](./cmwatersubmersionevent/date.md)
  The time and date of the event.
- [var state: CMWaterSubmersionEvent.State](./cmwatersubmersionevent/state-swift.property.md)
  The new submersion state.
- [CMWaterSubmersionEvent.State](./cmwatersubmersionevent/state-swift.enum.md)
  The device’s submersion state.
### Initializers
- [init?(coder: NSCoder)](./cmwatersubmersionevent/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Water submersion
- [Accessing submersion data](./accessing-submersion-data.md)
  Use a water-submersion manager to receive water pressure, temperature, and depth data on Apple Watch Ultra.
- [class CMWaterSubmersionManager](./cmwatersubmersionmanager.md)
  An object for managing the collection of pressure and temperature data during submersion.
- [protocol CMWaterSubmersionManagerDelegate](./cmwatersubmersionmanagerdelegate.md)
  A delegate that receives updates about ambient pressure, water pressure, water temperature, and submersion events.
- [class CMWaterSubmersionMeasurement](./cmwatersubmersionmeasurement.md)
  An update that contains data about the pressure and depth.
- [class CMWaterTemperature](./cmwatertemperature.md)
  An update that contains data about the water temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent)*