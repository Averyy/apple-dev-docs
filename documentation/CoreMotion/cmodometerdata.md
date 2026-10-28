# CMOdometerData

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

A class that represents odometer data for workouts.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class CMOdometerData
```

```objc
@interface CMOdometerData : NSObject
```

## Overview

To get the measurements, use the [`speed`](./cmodometerdata/speed.md) and [`slope`](./cmodometerdata/slope-96hlt.md) properties. To compute distances, use the [`deltaDistance`](./cmodometerdata/deltadistance.md) and [`deltaAltitude`](./cmodometerdata/deltaaltitude.md) properties.

## Topics

### Getting speed and slope
- [var speed: CLLocationSpeed](./cmodometerdata/speed.md)
  The instantaneous velocity of the device, measured in meters per second.
- [var slope: Double?](./cmodometerdata/slope-9h3m4.md)
  The slope at the location toward the direction of travel, measured in degrees.
- [var maxAbsSlope: Double?](./cmodometerdata/maxabsslope-9mnfd.md)
  The maximum absolute slope at the location toward all directions, measured in degrees.
- [slope](./cmodometerdata/slope-96hlt.md)
  The slope at the location toward the direction of travel, measured in degrees.
- [maxAbsSlope](./cmodometerdata/maxabsslope-96ulr.md)
  The maximum absolute slope at the location toward all directions, measured in degrees.
### Getting date and times
- [var startDate: Date](./cmodometerdata/startdate.md)
  The time that the device starts recording the odometer data.
- [var endDate: Date](./cmodometerdata/enddate.md)
  The time that the device stops recording the odometer data.
- [var gpsDate: Date](./cmodometerdata/gpsdate.md)
  The time of the GPS measurement associated with the location.
### Measuring distances
- [var deltaDistance: CLLocationDistance](./cmodometerdata/deltadistance.md)
  The change in distance that the user travels since the last location, measured in meters.
- [var deltaAltitude: CLLocationDistance](./cmodometerdata/deltaaltitude.md)
  The change in altitude above mean sea level associated with the location, measured in meters.
### Getting the location accuracy
- [var speedAccuracy: CLLocationSpeedAccuracy](./cmodometerdata/speedaccuracy.md)
  The accuracy of the speed value.
- [var verticalAccuracy: CLLocationAccuracy](./cmodometerdata/verticalaccuracy.md)
  The validity of the altitude values and their estimated uncertainty, measured in meters.
- [var deltaDistanceAccuracy: CLLocationAccuracy](./cmodometerdata/deltadistanceaccuracy.md)
  The accuracy of the change in distance value.
### Getting the device
- [var originDevice: CMOdometerOriginDevice](./cmodometerdata/origindevice.md)
  The device that measures the data.
- [enum CMOdometerOriginDevice](./cmodometerorigindevice.md)
  The device that the odometer sample originates from.
### Initializers
- [init?(coder: NSCoder)](./cmodometerdata/init%28coder%29.md)

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Pedometer and fitness
- [class CMPedometer](./cmpedometer.md)
  An object for fetching the system-generated live walking data.
- [class CMPedometerData](./cmpedometerdata.md)
  Information about the distance traveled by a user on foot.
- [class CMPedometerEvent](./cmpedometerevent.md)
  A change in the user’s pedestrian activity.
- [class CMStepCounter](./cmstepcounter.md)
  The number of steps the user has taken with the device.
- [class CMHighFrequencyHeartRateData](./cmhighfrequencyheartratedata.md)
  A class that represents heart rate data collected at 1 Hz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmodometerdata)*