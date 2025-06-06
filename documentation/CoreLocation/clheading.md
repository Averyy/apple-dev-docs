# CLHeading

**Framework**: Corelocation  
**Kind**: class

The orientation of the user’s device, relative to true or magnetic north.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- watchOS 2.0+

## Declaration

```swift
class CLHeading
```

#### Overview

A [`CLHeading`](clheading.md) object contains computed values for the device’s azimuth (orientation) relative to true or magnetic north. It also includes the raw data for the three-dimensional vector used to compute those values. A navigation app might use the information to rotate a map so that it reflects the direction that the user is facing.

Typically, you don’t create instances of this class yourself, nor do you subclass it. Instead, you receive instances of this class through the delegate assigned to the [`CLLocationManager`](cllocationmanager.md) object whose [`startUpdatingHeading()`](cllocationmanager/startupdatingheading().md) method you called.

> **Note**:  If you want heading objects to contain valid data for the [`trueHeading`](clheading/trueheading.md) property, configure your location manager object to deliver location updates. You can start the delivery of these updates by calling the location manager object’s [`startUpdatingLocation()`](cllocationmanager/startupdatinglocation().md) method.

## Topics

### Getting the heading values
- [var magneticHeading: CLLocationDirection](clheading/magneticheading.md)
  The heading (measured in degrees) relative to magnetic north.
- [var trueHeading: CLLocationDirection](clheading/trueheading.md)
  The heading (measured in degrees) relative to true north.
- [var headingAccuracy: CLLocationDirection](clheading/headingaccuracy.md)
  The maximum deviation (measured in degrees) between the reported heading and the true geomagnetic heading.
### Getting the raw heading data
- [var x: CLHeadingComponentValue](clheading/x.md)
  The geomagnetic data (measured in microteslas) for the x-axis.
- [var y: CLHeadingComponentValue](clheading/y.md)
  The geomagnetic data (measured in microteslas) for the y-axis.
- [var z: CLHeadingComponentValue](clheading/z.md)
  The geomagnetic data (measured in microteslas) for the z-axis.
- [typealias CLHeadingComponentValue](clheadingcomponentvalue.md)
  A type used to report magnetic differences reported by the onboard hardware.
### Getting the event timestamp
- [var timestamp: Date](clheading/timestamp.md)
  The time at which this heading was determined.

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

- [Getting heading and course information](getting-heading-and-course-information.md)
  Use a device’s orientation and course information for navigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreLocation/clheading)*