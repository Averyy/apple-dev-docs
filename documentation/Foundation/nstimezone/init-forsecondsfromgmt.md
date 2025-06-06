# init(forSecondsFromGMT:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

A time zone object offset from Greenwich Mean Time by `seconds`.

#### Discussion

The name of the new time zone is GMT +/– the offset, in hours and minutes. Time zones created with this method never have daylight savings, and the offset is constant no matter the date.

## Parameters

- `seconds`: The number of seconds by which the new time zone is offset from GMT.

## See Also

- [init?(name: String)](nstimezone/init(name:).md)
  Returns a time zone initialized with a given identifier.
- [init?(name: String, data: Data?)](nstimezone/init(name:data:).md)
  Initializes a time zone with a given identifier and time zone data.
- [convenience init?(abbreviation: String)](nstimezone/init(abbreviation:).md)
  Returns the time zone object identified by a given abbreviation.
- [class var knownTimeZoneNames: [String]](nstimezone/knowntimezonenames.md)
  Returns an array of strings listing the IDs of all the time zones known to the system.
- [class var abbreviationDictionary: [String : String]](nstimezone/abbreviationdictionary.md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/init(forsecondsfromgmt:))*