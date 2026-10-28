# secondsFromGMT(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the difference in seconds between the receiver and Greenwich Mean Time at a given date.

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
func secondsFromGMT(for aDate: Date) -> Int
```

```objc
- (NSInteger) secondsFromGMTForDate:(NSDate *) aDate;
```

## Return Value

The difference in seconds between the receiver and Greenwich Mean Time at `aDate`.

## Discussion

The difference may be different from the current difference if the time zone changes its offset from GMT at different points in the year—for example, the U.S. time zones change with daylight saving time.

## Parameters

- `aDate`: The date against which to test the receiver.

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
- [var data: Data](./data.md)
  The data that stores the information used by the receiver.
- [class var timeZoneDataVersion: String](./timezonedataversion.md)
  Returns the time zone data version.
- [NSTimeZone.NameStyle](./namestyle.md)
  Constants you use to specify a style when presenting time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/secondsfromgmt(for:))*