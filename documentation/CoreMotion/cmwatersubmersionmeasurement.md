# CMWaterSubmersionMeasurement

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

An update that contains data about the pressure and depth.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class CMWaterSubmersionMeasurement
```

```objc
@interface CMWaterSubmersionMeasurement : NSObject
```

## Topics

### Accessing the data
- [var date: Date](./cmwatersubmersionmeasurement/date.md)
  The time and date when the system recorded the measurements.
- [var depth: Measurement<UnitLength>?](./cmwatersubmersionmeasurement/depth.md)
  The depth under water.
- [var pressure: Measurement<UnitPressure>?](./cmwatersubmersionmeasurement/pressure.md)
  The water pressure.
- [var surfacePressure: Measurement<UnitPressure>](./cmwatersubmersionmeasurement/surfacepressure.md)
  The surface air pressure.
- [var submersionState: CMWaterSubmersionMeasurement.DepthState](./cmwatersubmersionmeasurement/submersionstate.md)
  The depth state.
- [CMWaterSubmersionMeasurement.DepthState](./cmwatersubmersionmeasurement/depthstate.md)
  A state based on the device’s depth under water.
### Initializers
- [init?(coder: NSCoder)](./cmwatersubmersionmeasurement/init%28coder%29.md)

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
- [class CMWaterSubmersionEvent](./cmwatersubmersionevent.md)
  An event indicating that the device’s submersion state has changed.
- [class CMWaterTemperature](./cmwatertemperature.md)
  An update that contains data about the water temperature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement)*