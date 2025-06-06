# timeZoneDataVersion

**Framework**: Foundation  
**Kind**: property

Returns the time zone data version.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var timeZoneDataVersion: String { get }
```

#### Return Value

A string containing the time zone data version.

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
- [NSTimeZone.NameStyle](nstimezone/namestyle.md)
  Constants you use to specify a style when presenting time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/timezonedataversion)*