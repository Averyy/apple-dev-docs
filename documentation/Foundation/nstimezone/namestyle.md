# NSTimeZone.NameStyle

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSTimeZoneNameStyle : NSInteger;
```

## Topics

### Constants
- [NSTimeZone.NameStyle.standard](./namestyle/standard.md)
  Specifies a standard name style. For example, “Central Standard Time” for Central Time.
- [NSTimeZone.NameStyle.shortStandard](./namestyle/shortstandard.md)
  Specifies a short name style. For example, “CST” for Central Time.
- [NSTimeZone.NameStyle.daylightSaving](./namestyle/daylightsaving.md)
  Specifies a daylight saving name style. For example, “Central Daylight Time” for Central Time.
- [NSTimeZone.NameStyle.shortDaylightSaving](./namestyle/shortdaylightsaving.md)
  Specifies a short daylight saving name style.  For example, “CDT” for Central Time.
- [NSTimeZone.NameStyle.generic](./namestyle/generic.md)
  Specifies a generic name style. For example, “Central Time” for Central Time.
- [NSTimeZone.NameStyle.shortGeneric](./namestyle/shortgeneric.md)
  Specifies a generic time zone name. For example, “CT” for Central Time.
### Initializers
- [init?(rawValue: Int)](./namestyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Time Zone Information
- [var name: String](./name.md)
  The geopolitical region ID that identifies the receiver.
- [var abbreviation: String?](./abbreviation.md)
  The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).
- [func abbreviation(for: Date) -> String?](./abbreviation%28for%29.md)
  Returns the abbreviation for the receiver at a given date.
- [var secondsFromGMT: Int](./secondsfromgmt.md)
  The current difference in seconds between the receiver and Greenwich Mean Time.
- [func secondsFromGMT(for: Date) -> Int](./secondsfromgmt%28for%29.md)
  Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.
- [var data: Data](./data.md)
  The data that stores the information used by the receiver.
- [class var timeZoneDataVersion: String](./timezonedataversion.md)
  Returns the time zone data version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/namestyle)*