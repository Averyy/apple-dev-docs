# abbreviation

**Framework**: Foundation  
**Kind**: property

The abbreviation for the receiver, such as “EDT” (Eastern Daylight Time).

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
var abbreviation: String? { get }
```

#### Discussion

Invokes [`abbreviation(for:)`](nstimezone/abbreviation(for:).md) with the current date as the argument.

## See Also

- [var name: String](nstimezone/name.md)
  The geopolitical region ID that identifies the receiver.
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
- [NSTimeZone.NameStyle](nstimezone/namestyle.md)
  Constants you use to specify a style when presenting time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/abbreviation)*