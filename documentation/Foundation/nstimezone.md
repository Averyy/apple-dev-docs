# NSTimeZone

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

Information about standard time conventions associated with a specific geopolitical region.

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
class NSTimeZone
```

```objc
@interface NSTimeZone : NSObject
```

#### Overview

In Swift, this type bridges to [`TimeZone`](./timezone.md); use [`NSTimeZone`](./nstimezone.md) when you need reference semantics or other Foundation-specific behavior.

Time zones represent the standard time policies for a geopolitical region. Time zones have identifiers like “America/Los_Angeles” and can also be identified by abbreviations, such as PST for Pacific Standard Time. You can create time zone objects by ID with [`init(name:)`](./nstimezone/init%28name%29.md) and by abbreviation with [`init(abbreviation:)`](./nstimezone/init%28abbreviation%29.md).

> **Note**:  Time zone database entries such as “America/Los_Angeles” are IDs, not names. An example of a time zone name is “Pacific Daylight Time”. Although many [`NSTimeZone`](./nstimezone.md) symbols include the word “name”, they actually refer to IDs.

Time zones can also represent a temporal offset—either plus or minus—from Greenwich Mean Time (GMT). For example, the temporal offset of Pacific Standard Time is 8 hours behind Greenwich Mean Time (GMT-8). You can create time zone objects with a temporal offset by using [`init(forSecondsFromGMT:)`](./nstimezone/init%28forsecondsfromgmt%29.md).

You typically work with system time zones rather than creating time zones by identifier or by offset. The [`system`](./nstimezone/system.md) class property returns the time zone currently used by the system, if known. This value is cached once the property is accessed and doesn’t reflect any system time zone changes until you call the [`resetSystemTimeZone()`](./nstimezone/resetsystemtimezone%28%29.md) method. The [`local`](./nstimezone/local.md) class property returns an autoupdating proxy object that always returns the current time zone used by the system. You can also set the [`default`](./nstimezone/default.md) class property to make your app run as if it were in a different time zone than the system.

> 💡 **Tip**:  You can’t use [`NSTimeZone`](./nstimezone.md) APIs to change the time zone of the device or of other apps.

[`NSTimeZone`](./nstimezone.md) is *toll-free bridged* with its Core Foundation counterpart, [`CFTimeZone`](../CoreFoundation/cftimezone.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`TimeZone`](./timezone.md) structure, which bridges to the [`NSTimeZone`](./nstimezone.md) class. For more information about value types, see [Working with Foundation Types](../Swift/working-with-foundation-types.md).

## Topics

### Working with System Time Zones
- [class var local: TimeZone](./nstimezone/local.md)
  An object that tracks the current system time zone.
- [class var system: TimeZone](./nstimezone/system.md)
  The time zone currently used by the system.
- [class func resetSystemTimeZone()](./nstimezone/resetsystemtimezone%28%29.md)
  Clears any time zone value cached for the [`system`](./nstimezone/system.md) property.
- [class var `default`: TimeZone](./nstimezone/default.md)
  The default time zone for the current app.
### Creating Time Zones
- [init?(name: String)](./nstimezone/init%28name%29.md)
  Returns a time zone initialized with a given identifier.
- [init?(name: String, data: Data?)](./nstimezone/init%28name,data%29.md)
  Initializes a time zone with a given identifier and time zone data.
- [convenience init?(abbreviation: String)](./nstimezone/init%28abbreviation%29.md)
  Returns the time zone object identified by a given abbreviation.
- [convenience init(forSecondsFromGMT: Int)](./nstimezone/init%28forsecondsfromgmt%29.md)
  Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [class var knownTimeZoneNames: [String]](./nstimezone/knowntimezonenames.md)
  Returns an array of strings listing the IDs of all the time zones known to the system.
- [class var abbreviationDictionary: [String : String]](./nstimezone/abbreviationdictionary.md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
### Getting Time Zone Information
- [var name: String](./nstimezone/name.md)
  The geopolitical region ID that identifies the receiver.
- [var abbreviation: String?](./nstimezone/abbreviation.md)
  The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).
- [func abbreviation(for: Date) -> String?](./nstimezone/abbreviation%28for%29.md)
  Returns the abbreviation for the receiver at a given date.
- [var secondsFromGMT: Int](./nstimezone/secondsfromgmt.md)
  The current difference in seconds between the receiver and Greenwich Mean Time.
- [func secondsFromGMT(for: Date) -> Int](./nstimezone/secondsfromgmt%28for%29.md)
  Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.
- [var data: Data](./nstimezone/data.md)
  The data that stores the information used by the receiver.
- [class var timeZoneDataVersion: String](./nstimezone/timezonedataversion.md)
  Returns the time zone data version.
- [NSTimeZone.NameStyle](./nstimezone/namestyle.md)
  Constants you use to specify a style when presenting time zone names.
### Working with Daylight Savings
- [var isDaylightSavingTime: Bool](./nstimezone/isdaylightsavingtime.md)
  A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [func isDaylightSavingTime(for: Date) -> Bool](./nstimezone/isdaylightsavingtime%28for%29.md)
  Indicates whether the receiver uses daylight saving time on a given date.
- [var daylightSavingTimeOffset: TimeInterval](./nstimezone/daylightsavingtimeoffset.md)
  The current daylight saving time offset of the receiver.
- [func daylightSavingTimeOffset(for: Date) -> TimeInterval](./nstimezone/daylightsavingtimeoffset%28for%29.md)
  Returns the daylight saving time offset for a given date.
- [var nextDaylightSavingTimeTransition: Date?](./nstimezone/nextdaylightsavingtimetransition.md)
  The date of the next daylight saving time transition for the receiver.
- [func nextDaylightSavingTimeTransition(after: Date) -> Date?](./nstimezone/nextdaylightsavingtimetransition%28after%29.md)
  Returns the next daylight saving time transition after a given date.
### Comparing Time Zones
- [func isEqual(to: TimeZone) -> Bool](./nstimezone/isequal%28to%29.md)
  Indicates whether the receiver has the same name and data as the specified time zone.
### Describing Time Zones
- [func localizedName(NSTimeZone.NameStyle, locale: Locale?) -> String?](./nstimezone/localizedname%28_,locale%29.md)
  Returns the localized name of the time zone.
- [var description: String](./nstimezone/description.md)
  A textual description of the time zone including the name, abbreviation, offset from GMT, and whether or not daylight saving time is currently in effect.
### Recognizing Notifications
- [static let NSSystemTimeZoneDidChange: NSNotification.Name](./nsnotification/name-swift.struct/nssystemtimezonedidchange.md)
  A notification posted when the time zone changes.
### Initializers
- [init?(coder: NSCoder)](./nstimezone/init%28coder%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone)*