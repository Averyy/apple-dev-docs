# init(name:)

**Framework**: Foundation  
**Kind**: init

Returns a time zone initialized with a given identifier.

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
init?(name tzName: String)
```

#### Return Value

A time zone object initialized with the identifier `tzName`.

#### Discussion

If `tzName` is a known identifier, this method calls [`init(name:data:)`](nstimezone/init(name:data:).md) with the appropriate data object.

## Parameters

- `tzName`: The identifier for the time zone. Providing   for this parameter raises an invalid argument exception.

## See Also

- [init?(name: String, data: Data?)](nstimezone/init(name:data:).md)
  Initializes a time zone with a given identifier and time zone data.
- [convenience init?(abbreviation: String)](nstimezone/init(abbreviation:).md)
  Returns the time zone object identified by a given abbreviation.
- [convenience init(forSecondsFromGMT: Int)](nstimezone/init(forsecondsfromgmt:).md)
  Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [class var knownTimeZoneNames: [String]](nstimezone/knowntimezonenames.md)
  Returns an array of strings listing the IDs of all the time zones known to the system.
- [class var abbreviationDictionary: [String : String]](nstimezone/abbreviationdictionary.md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/init(name:))*