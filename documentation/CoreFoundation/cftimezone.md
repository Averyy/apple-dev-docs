# CFTimeZone

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFTimeZone
```

#### Overview

CFTimeZone defines the behavior of time zone objects. Time zone objects represent geopolitical regions. Consequently, these objects have names for these regions. Time zone objects also represent a temporal offset, either plus or minus, from Greenwich Mean Time (GMT) and an abbreviation (such as PST for Pacific Standard Time).

CFTimeZone provides several functions to create time zone objects: [`CFTimeZoneCreateWithName(_:_:_:)`](cftimezonecreatewithname(_:_:_:).md) and [`CFTimeZoneCreateWithTimeIntervalFromGMT(_:_:)`](cftimezonecreatewithtimeintervalfromgmt(_:_:).md). CFTimeZone also permits you to set the default time zone within your application using the [`CFTimeZoneSetDefault(_:)`](cftimezonesetdefault(_:).md) function. You can access this default time zone at any time with the [`CFTimeZoneCopyDefault()`](cftimezonecopydefault().md) function.

CFTimeZone is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSTimeZone`](https://developer.apple.com/documentation/Foundation/NSTimeZone). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSTimeZone *` parameter, you can pass in a `CFTimeZoneRef`, and in a function where you see a `CFTimeZoneRef` parameter, you can pass in an NSTimeZone instance. This fact also applies to concrete subclasses of NSTimeZone. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a Time Zone
- [func CFTimeZoneCreateWithName(CFAllocator!, CFString!, Bool) -> CFTimeZone!](cftimezonecreatewithname(_:_:_:).md)
  Returns the time zone object identified by a given name or abbreviation.
- [func CFTimeZoneCreateWithTimeIntervalFromGMT(CFAllocator!, CFTimeInterval) -> CFTimeZone!](cftimezonecreatewithtimeintervalfromgmt(_:_:).md)
  Returns a time zone object for the specified time interval offset from Greenwich Mean Time (GMT).
- [func CFTimeZoneCreate(CFAllocator!, CFString!, CFData!) -> CFTimeZone!](cftimezonecreate(_:_:_:).md)
  Creates a time zone with a given name and data.
### System and Default Time Zones and Information
- [func CFTimeZoneCopyAbbreviationDictionary() -> CFDictionary!](cftimezonecopyabbreviationdictionary().md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [func CFTimeZoneCopyAbbreviation(CFTimeZone!, CFAbsoluteTime) -> CFString!](cftimezonecopyabbreviation(_:_:).md)
  Returns the abbreviation of a time zone at a specified date.
- [func CFTimeZoneCopyDefault() -> CFTimeZone!](cftimezonecopydefault().md)
  Returns the default time zone set for your application.
- [func CFTimeZoneCopySystem() -> CFTimeZone!](cftimezonecopysystem().md)
  Returns the time zone currently used by the system.
- [func CFTimeZoneSetDefault(CFTimeZone!)](cftimezonesetdefault(_:).md)
  Sets the default time zone for your application the given time zone.
- [func CFTimeZoneCopyKnownNames() -> CFArray!](cftimezonecopyknownnames().md)
  Returns an array of strings containing the names of all the time zones known to the system.
- [func CFTimeZoneResetSystem()](cftimezoneresetsystem().md)
  Clears the previously determined system time zone, if any.
- [func CFTimeZoneSetAbbreviationDictionary(CFDictionary!)](cftimezonesetabbreviationdictionary(_:).md)
  Sets the abbreviation dictionary to a given dictionary.
### Getting Information About Time Zones
- [func CFTimeZoneGetName(CFTimeZone!) -> CFString!](cftimezonegetname(_:).md)
  Returns the geopolitical region name that identifies a given time zone.
- [func CFTimeZoneCopyLocalizedName(CFTimeZone!, CFTimeZoneNameStyle, CFLocale!) -> CFString!](cftimezonecopylocalizedname(_:_:_:).md)
  Returns the localized name of a given time zone.
- [func CFTimeZoneGetSecondsFromGMT(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval](cftimezonegetsecondsfromgmt(_:_:).md)
  Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.
- [func CFTimeZoneGetData(CFTimeZone!) -> CFData!](cftimezonegetdata(_:).md)
  Returns the data that stores the information used by a time zone.
### Getting Daylight Savings Time Information
- [func CFTimeZoneIsDaylightSavingTime(CFTimeZone!, CFAbsoluteTime) -> Bool](cftimezoneisdaylightsavingtime(_:_:).md)
  Returns whether or not a time zone is in daylight savings time at a specified date.
- [func CFTimeZoneGetDaylightSavingTimeOffset(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval](cftimezonegetdaylightsavingtimeoffset(_:_:).md)
  Returns the daylight saving time offset for a time zone at a given time.
- [func CFTimeZoneGetNextDaylightSavingTimeTransition(CFTimeZone!, CFAbsoluteTime) -> CFAbsoluteTime](cftimezonegetnextdaylightsavingtimetransition(_:_:).md)
  Returns the time in a given time zone of the next daylight saving time transition after a given time.
### Getting the CFTimeZone Type ID
- [func CFTimeZoneGetTypeID() -> CFTypeID](cftimezonegettypeid().md)
  Returns the type identifier for the CFTimeZone opaque type.
### Data Types
- [enum CFTimeZoneNameStyle](cftimezonenamestyle.md)
  Index type for constants used to specify styles of time zone names.
### Constants
- [Notification Name](notification-name.md)
  Name of the notification posted when the time zone changes.
- [Time Zone Name Styles](time_zone_name_styles.md)
  Constants to specify styles for time zone names.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Date and Time Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/CFDatesAndTimes.html#//apple_ref/doc/uid/10000125i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezone)*