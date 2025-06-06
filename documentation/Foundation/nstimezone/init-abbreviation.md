# init(abbreviation:)

**Framework**: Foundation  
**Kind**: init

Returns the time zone object identified by a given abbreviation.

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
convenience init?(abbreviation: String)
```

#### Return Value

The time zone object identified by `abbreviation` determined by resolving the abbreviation to a name using the abbreviation dictionary and then returning the time zone for that name. Returns `nil` if there is no match for `abbreviation`.

#### Discussion

In general, you are discouraged from using abbreviations except for unique instances such as “GMT”. Time Zone abbreviations are not standardized and so a given abbreviation may have multiple meanings—for example, “EST” refers to Eastern Time in both the United States and Australia

## Parameters

- `abbreviation`: An abbreviation for a time zone.

## See Also

- [Date and Time Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i)
- [init?(name: String)](nstimezone/init(name:).md)
  Returns a time zone initialized with a given identifier.
- [init?(name: String, data: Data?)](nstimezone/init(name:data:).md)
  Initializes a time zone with a given identifier and time zone data.
- [convenience init(forSecondsFromGMT: Int)](nstimezone/init(forsecondsfromgmt:).md)
  Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [class var knownTimeZoneNames: [String]](nstimezone/knowntimezonenames.md)
  Returns an array of strings listing the IDs of all the time zones known to the system.
- [class var abbreviationDictionary: [String : String]](nstimezone/abbreviationdictionary.md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/init(abbreviation:))*