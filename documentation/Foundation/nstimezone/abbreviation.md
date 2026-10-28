# abbreviation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSString * abbreviation;
```

## Discussion

Invokes [`abbreviation(for:)`](./abbreviation%28for%29.md) with the current date as the argument.

## See Also

### Getting Time Zone Information
- [var name: String](./name.md)
  The geopolitical region ID that identifies the receiver.
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
- [NSTimeZone.NameStyle](./namestyle.md)
  Constants you use to specify a style when presenting time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/abbreviation)*