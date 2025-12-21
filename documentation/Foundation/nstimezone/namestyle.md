# NSTimeZone.NameStyle

**Framework**: Foundation  
**Kind**: enum

Constants you use to specify a style when presenting time zone names.

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
enum NameStyle
```

## Topics

### Constants
- [NSTimeZone.NameStyle.standard](nstimezone/namestyle/standard.md)
  Specifies a standard name style. For example, “Central Standard Time” for Central Time.
- [NSTimeZone.NameStyle.shortStandard](nstimezone/namestyle/shortstandard.md)
  Specifies a short name style. For example, “CST” for Central Time.
- [NSTimeZone.NameStyle.daylightSaving](nstimezone/namestyle/daylightsaving.md)
  Specifies a daylight saving name style. For example, “Central Daylight Time” for Central Time.
- [NSTimeZone.NameStyle.shortDaylightSaving](nstimezone/namestyle/shortdaylightsaving.md)
  Specifies a short daylight saving name style.  For example, “CDT” for Central Time.
- [NSTimeZone.NameStyle.generic](nstimezone/namestyle/generic.md)
  Specifies a generic name style. For example, “Central Time” for Central Time.
- [NSTimeZone.NameStyle.shortGeneric](nstimezone/namestyle/shortgeneric.md)
  Specifies a generic time zone name. For example, “CT” for Central Time.
### Initializers
- [init?(rawValue: Int)](nstimezone/namestyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var name: String](nstimezone/name.md)
  The geopolitical region ID that identifies the receiver.
- [var abbreviation: String?](nstimezone/abbreviation.md)
  The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).
- [func abbreviation(for: Date) -> String?](nstimezone/abbreviation(for:).md)
  Returns the abbreviation for the receiver at a given date.
- [var secondsFromGMT: Int](nstimezone/secondsfromgmt.md)
  The current difference in seconds between the receiver and Greenwich Mean Time.
- [func secondsFromGMT(for: Date) -> Int](nstimezone/secondsfromgmt(for:).md)
  Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.
- [var data: Data](nstimezone/data.md)
  The data that stores the information used by the receiver.
- [class var timeZoneDataVersion: String](nstimezone/timezonedataversion.md)
  Returns the time zone data version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/namestyle)*