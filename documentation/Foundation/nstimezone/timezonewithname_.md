# timeZoneWithName:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the time zone object identified by a given identifier.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) timeZoneWithName:(NSString *) tzName;
```

## Return Value

The time zone in the information directory with a name matching `tzName`. Returns `nil` if there is no match for the name.

## Parameters

- `tzName`: The ID for the time zone.

## See Also

### Creating Time Zones
- [+ timeZoneWithName:data:](./timezonewithname_data_.md)
  Returns the time zone with a given identifier whose data has been initialized using given data.
- [init?(name: String)](./init%28name%29.md)
  Returns a time zone initialized with a given identifier.
- [init?(name: String, data: Data?)](./init%28name,data%29.md)
  Initializes a time zone with a given identifier and time zone data.
- [convenience init?(abbreviation: String)](./init%28abbreviation%29.md)
  Returns the time zone object identified by a given abbreviation.
- [convenience init(forSecondsFromGMT: Int)](./init%28forsecondsfromgmt%29.md)
  Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [class var knownTimeZoneNames: [String]](./knowntimezonenames.md)
  Returns an array of strings listing the IDs of all the time zones known to the system.
- [class var abbreviationDictionary: [String : String]](./abbreviationdictionary.md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/timezonewithname:)*