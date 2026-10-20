# NSDateInterval

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object representing the span of time between a specific start date and end date.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class NSDateInterval
```

```objc
@interface NSDateInterval : NSObject
```

#### Overview

In Swift, this object bridges to [`DateInterval`](./dateinterval.md); use [`NSDateInterval`](./nsdateinterval.md) when you need reference semantics or other Foundation-specific behavior.

An `NSDateInterval` object represents a closed interval between two dates. The `NSDateInterval` class provides a programmatic interface for calculating the duration of a time interval and determining whether a date falls within it, as well as comparing date intervals and checking to see whether they intersect.

An `NSDateInterval` object consists of a [`startDate`](./nsdateinterval/startdate.md) and an [`endDate`](./nsdateinterval/enddate.md). The [`startDate`](./nsdateinterval/startdate.md) and [`endDate`](./nsdateinterval/enddate.md) of a date interval can be equal, in which case its [`duration`](./nsdateinterval/duration.md) is `0`. However, [`endDate`](./nsdateinterval/enddate.md) cannot occur earlier than [`startDate`](./nsdateinterval/startdate.md).

You can use the [`DateIntervalFormatter`](./dateintervalformatter.md) class to create string representations of `NSDateInterval` objects that are suitable for display in the current locale.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`DateInterval`](./dateinterval.md) structure, which bridges to the `NSDateInterval` class. For more information about value types, see [Working with Foundation Types](../Swift/working-with-foundation-types.md).

## Topics

### Creating Date Intervals
- [convenience init()](./nsdateinterval/init%28%29.md)
  Initializes a date interval by setting the start and end date to the current date.
- [init(start: Date, duration: TimeInterval)](./nsdateinterval/init%28start,duration%29.md)
  Initializes a date interval with a given start date and duration.
- [convenience init(start: Date, end: Date)](./nsdateinterval/init%28start,end%29.md)
  Initializes a date interval from a given start date and end date.
- [init(coder: NSCoder)](./nsdateinterval/init%28coder%29.md)
  Returns a date interval initialized from data in the given unarchiver.
### Accessing Start Date, End Date, and Duration
- [var startDate: Date](./nsdateinterval/startdate.md)
  The start date of the date interval.
- [var endDate: Date](./nsdateinterval/enddate.md)
  The end date of the date interval.
- [var duration: TimeInterval](./nsdateinterval/duration.md)
  The duration of the date interval.
### Comparing Date Intervals
- [func compare(DateInterval) -> ComparisonResult](./nsdateinterval/compare%28_%29.md)
  Compares the receiver with the specified date interval.
- [func isEqual(to: DateInterval) -> Bool](./nsdateinterval/isequal%28to%29.md)
  Indicates whether the receiver is equal to the specified date interval.
### Determining Intersections
- [func intersects(DateInterval) -> Bool](./nsdateinterval/intersects%28_%29.md)
  Indicates whether the receiver intersects with the specified date interval.
- [func intersection(with: DateInterval) -> DateInterval?](./nsdateinterval/intersection%28with%29.md)
  Returns the intersection between the receiver and the specified date interval.
### Determining Whether a Date Occurs Within a Date Interval
- [func contains(Date) -> Bool](./nsdateinterval/contains%28_%29.md)
  Indicates whether the receiver contains the specified date.
### Initializers
- [init(startDate: Date, duration: TimeInterval)](./nsdateinterval/init%28startdate,duration%29.md)
- [convenience init(startDate: Date, endDate: Date)](./nsdateinterval/init%28startdate,enddate%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdateinterval)*