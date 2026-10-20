# timeZoneDataVersion

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, copy, readonly) NSString * timeZoneDataVersion;
```

#### Return Value

A string containing the time zone data version.

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
- [NSTimeZone.NameStyle](./namestyle.md)
  Constants you use to specify a style when presenting time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/timezonedataversion)*