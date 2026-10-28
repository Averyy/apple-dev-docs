# init(forSecondsFromGMT:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.

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
convenience init(forSecondsFromGMT seconds: Int)
```

```objc
+ (instancetype) timeZoneForSecondsFromGMT:(NSInteger) seconds;
```

## Return Value

A time zone object offset from Greenwich Mean Time by `seconds`.

## Discussion

The name of the new time zone is GMT +/– the offset, in hours and minutes. Time zones created with this method never have daylight savings, and the offset is constant no matter the date.

## Parameters

- `seconds`: The number of seconds by which the new time zone is offset from GMT.

## See Also

### Creating Time Zones
- [init?(name: String)](./init%28name%29.md)
  Returns a time zone initialized with a given identifier.
- [init?(name: String, data: Data?)](./init%28name,data%29.md)
  Initializes a time zone with a given identifier and time zone data.
- [convenience init?(abbreviation: String)](./init%28abbreviation%29.md)
  Returns the time zone object identified by a given abbreviation.
- [class var knownTimeZoneNames: [String]](./knowntimezonenames.md)
  Returns an array of strings listing the IDs of all the time zones known to the system.
- [class var abbreviationDictionary: [String : String]](./abbreviationdictionary.md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [+ timeZoneWithName:data:](./timezonewithname_data_.md)
  Returns the time zone with a given identifier whose data has been initialized using given data.
### Related Documentation
- [+ timeZoneWithName:](./timezonewithname_.md)
  Returns the time zone object identified by a given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/init(forsecondsfromgmt:))*