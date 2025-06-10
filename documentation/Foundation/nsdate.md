# NSDate

**Framework**: Foundation  
**Kind**: class

A representation of a specific point in time, independent of any calendar or time zone.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSDate
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Overview

In Swift, use this type when you need reference semantics or other Foundation-specific behavior.

[`NSDate`](nsdate.md) objects encapsulate a single point in time, independent of any particular calendrical system or time zone. Date objects are immutable, representing an invariant time interval relative to an absolute reference date (00:00:00 UTC on 1 January 2001).

The [`NSDate`](nsdate.md) class provides methods for comparing dates, calculating the time interval between two dates, and creating a new date from a time interval relative to another date. [`NSDate`](nsdate.md) objects can be used in conjunction with [`DateFormatter`](dateformatter.md) objects to create localized representations of dates and times, as well as with [`NSCalendar`](nscalendar.md) objects to perform calendar arithmetic.

[`NSDate`](nsdate.md) is  with its Core Foundation counterpart, [`CFDate`](https://developer.apple.com/documentation/CoreFoundation/CFDate). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`Date`](date.md) structure, which bridges to the [`NSDate`](nsdate.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

##### Subclassing Notes

You might subclass [`NSDate`](nsdate.md) in order to make it easier to work with a particular calendrical system, or to work with date and time values with a finer temporal granularity.

###### Methods to Override and Other Requirements

If you want to subclass [`NSDate`](nsdate.md) to obtain behavior different than that provided by the private or public subclasses, you must:

- Declare a suitable instance variable to hold the date and time value (relative to an absolute reference date)
- Override the [`timeIntervalSinceReferenceDate`](nsdate/timeintervalsincereferencedate-swift.property.md) instance method to provide the correct date and time value based on your instance variable
- Override [`init(timeIntervalSinceReferenceDate:)`](nsdate/init(timeintervalsincereferencedate:).md), one of the designated initializer methods
- If creating a subclass that represents a calendrical system, define methods that partition past and future periods into the units of this calendar
- Implement the methods required by the [`NSCopying`](nscopying.md) and [`NSCoding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WritingSwiftClassesWithObjective-CBehavior.html#//apple_ref/doc/uid/TP40014216-CH5-ID152) protocols, because [`NSDate`](nsdate.md) adopts these protocols

###### Special Considerations

Your subclass may use a different reference date than the absolute reference date used by [`NSDate`](nsdate.md) (00:00:00 UTC on 1 January 2001). If it does, it must still use the absolute reference date in its implementations of the methods [`timeIntervalSinceReferenceDate`](nsdate/timeintervalsincereferencedate-swift.property.md) and [`init(timeIntervalSinceReferenceDate:)`](nsdate/init(timeintervalsincereferencedate:).md). That is, the reference date referred to in the titles of these methods is the absolute reference date. If you do not use the absolute reference date in these methods, comparisons between [`NSDate`](nsdate.md) objects of your subclass and `NSDate` objects of a private subclass will not work.

## Topics

### Creating a Date
- [convenience init(timeInterval: TimeInterval, sinceDate: Date)](nsdate/init(timeinterval:sincedate:)-49cea.md)
  Creates and returns a date object set to a given number of seconds from the specified date.
### Initializing a Date
- [init()](nsdate/init.md)
  Returns a date object initialized to the current date and time.
- [convenience init(timeIntervalSinceNow: TimeInterval)](nsdate/init(timeintervalsincenow:).md)
  Returns a date object initialized relative to the current date and time by a given number of seconds.
- [convenience init(timeInterval: TimeInterval, sinceDate: Date)](nsdate/init(timeinterval:sincedate:)-71m1f.md)
  Returns a date object initialized relative to another given date by a given number of seconds.
- [init(timeIntervalSinceReferenceDate: TimeInterval)](nsdate/init(timeintervalsincereferencedate:).md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 2001 by a given number of seconds.
- [convenience init(timeIntervalSince1970: TimeInterval)](nsdate/init(timeintervalsince1970:).md)
  Returns a date object initialized relative to 00:00:00 UTC on 1 January 1970 by a given number of seconds.
- [init?(coder: NSCoder)](nsdate/init(coder:).md)
  Returns a date object initialized from data in the given unarchiver.
### Getting Temporal Boundaries
- [class var distantFuture: Date](nsdate/distantfuture.md)
  A date object representing a date in the distant future.
- [class var distantPast: Date](nsdate/distantpast.md)
  A date object representing a date in the distant past.
### Retrieving the Current Date
- [class var now: Date](nsdate/now.md)
  The current date and time, as of the time of access.
### Comparing Dates
- [func isEqual(to: Date) -> Bool](nsdate/isequal(to:).md)
  Returns a Boolean value that indicates whether a given object is a date that is exactly equal the receiver.
- [func earlierDate(Date) -> Date](nsdate/earlierdate(_:).md)
  Returns the earlier of the receiver and another given date.
- [func laterDate(Date) -> Date](nsdate/laterdate(_:).md)
  Returns the later of the receiver and another given date.
- [func compare(Date) -> ComparisonResult](nsdate/compare(_:).md)
  Indicates the temporal ordering of the receiver and another given date.
### Getting Time Intervals
- [func timeIntervalSince(Date) -> TimeInterval](nsdate/timeintervalsince(_:).md)
  Returns the interval between the receiver and another given date.
- [var timeIntervalSinceNow: TimeInterval](nsdate/timeintervalsincenow.md)
  The interval between the date object and the current date and time.
- [var timeIntervalSinceReferenceDate: TimeInterval](nsdate/timeintervalsincereferencedate-swift.property.md)
  The interval between the date object and 00:00:00 UTC on 1 January 2001.
- [var timeIntervalSince1970: TimeInterval](nsdate/timeintervalsince1970.md)
  The interval between the date object and 00:00:00 UTC on 1 January 1970.
- [class var timeIntervalSinceReferenceDate: TimeInterval](nsdate/timeintervalsincereferencedate-swift.type.property.md)
  The interval between 00:00:00 UTC on 1 January 2001 and the current date and time.
- [var NSTimeIntervalSince1970: Double](nstimeintervalsince1970.md)
  The number of seconds from 1 January 1970 to the reference date, 1 January 2001.
### Adding Time Intervals
- [func addingTimeInterval(TimeInterval) -> Self](nsdate/addingtimeinterval(_:).md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
### Describing Dates
- [var description: String](nsdate/description.md)
  A string representation of the date object.
- [func description(with: Any?) -> String](nsdate/description(with:).md)
  Returns a string representation of the date using the given locale.
- [var customPlaygroundQuickLook: PlaygroundQuickLook](nsdate/customplaygroundquicklook.md)
  A custom playground Quick Look for this object.
### Recognizing Notifications
- [static let NSSystemClockDidChange: NSNotification.Name](nsnotification/name-swift.struct/nssystemclockdidchange.md)
  A notification posted whenever the system clock is changed.
### Legacy Operations
- [class func date(withNaturalLanguageString: String) -> Any?](nsdate/date(withnaturallanguagestring:).md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(withNaturalLanguageString: String, locale: Any?) -> Any?](nsdate/date(withnaturallanguagestring:locale:).md)
  Creates and returns a date object set to the date and time specified by a given string.
- [class func date(with: String) -> Any](nsdate/date(with:).md)
  Creates and returns a date object with a date and time value specified by a given string in the international string representation format (`YYYY-MM-DD HH:MM:SS ±HHMM`).
- [convenience init?(string: String)](nsdate/init(string:).md)
  Returns a date object initialized with a date and time value specified by a given string in the international string representation format.
- [func addTimeInterval(TimeInterval) -> Any](nsdate/addtimeinterval(_:).md)
  Returns a new date object that is set to a given number of seconds relative to the receiver.
- [func date(withCalendarFormat: String?, timeZone: TimeZone?) -> NSCalendarDate](nsdate/date(withcalendarformat:timezone:).md)
  Converts the receiver to a calendar date with a given format string and time zone.
- [func description(withCalendarFormat: String?, timeZone: TimeZone?, locale: Any?) -> String?](nsdate/description(withcalendarformat:timezone:locale:).md)
  Returns a string representation of the date formatted as specified by given conversion specifiers.
### Initializers
- [convenience init(SRAbsoluteTime: SRAbsoluteTime)](nsdate/init(srabsolutetime:)-886t8.md)
- [convenience init(SRAbsoluteTime: SRAbsoluteTime)](nsdate/init(srabsolutetime:)-9wpl1.md)
### Instance Properties
- [var srAbsoluteTime: SRAbsoluteTime](nsdate/srabsolutetime.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CKRecordValue](../CloudKit/CKRecordValue-c.protocol.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate)*