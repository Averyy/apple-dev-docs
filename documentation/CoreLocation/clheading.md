# CLHeading

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

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

```objc
@interface CLHeading : NSObject
```

## Overview

A [`CLHeading`](./clheading.md) object contains computed values for the device’s azimuth (orientation) relative to true or magnetic north. It also includes the raw data for the three-dimensional vector used to compute those values. A navigation app might use the information to rotate a map so that it reflects the direction that the user is facing.

Typically, you don’t create instances of this class yourself, nor do you subclass it. Instead, you receive instances of this class through the delegate assigned to the [`CLLocationManager`](./cllocationmanager.md) object whose [`startUpdatingHeading()`](./cllocationmanager/startupdatingheading%28%29.md) method you called.

> **Note**:  If you want heading objects to contain valid data for the [`trueHeading`](./clheading/trueheading.md) property, configure your location manager object to deliver location updates. You can start the delivery of these updates by calling the location manager object’s [`startUpdatingLocation()`](./cllocationmanager/startupdatinglocation%28%29.md) method.

## Topics

### Getting the heading values
- [var magneticHeading: CLLocationDirection](./clheading/magneticheading.md)
  The heading (measured in degrees) relative to magnetic north.
- [var trueHeading: CLLocationDirection](./clheading/trueheading.md)
  The heading (measured in degrees) relative to true north.
- [var headingAccuracy: CLLocationDirection](./clheading/headingaccuracy.md)
  The maximum deviation (measured in degrees) between the reported heading and the true geomagnetic heading.
### Getting the raw heading data
- [var x: CLHeadingComponentValue](./clheading/x.md)
  The geomagnetic data (measured in microteslas) for the x-axis.
- [var y: CLHeadingComponentValue](./clheading/y.md)
  The geomagnetic data (measured in microteslas) for the y-axis.
- [var z: CLHeadingComponentValue](./clheading/z.md)
  The geomagnetic data (measured in microteslas) for the z-axis.
- [typealias CLHeadingComponentValue](./clheadingcomponentvalue.md)
  A type used to report magnetic differences reported by the onboard hardware.
### Getting the event timestamp
- [var timestamp: Date](./clheading/timestamp.md)
  The time at which this heading was determined.
### Initializers
- [init?(coder: NSCoder)](./clheading/init%28coder%29.md)

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

### Compass headings
- [Getting heading and course information](./getting-heading-and-course-information.md)
  Use a device’s orientation and course information for navigation.
- [protocol CLBodyIdentifiable](./clbodyidentifiable.md)
  A type that identifies a physical body or view for heading calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clheading)*