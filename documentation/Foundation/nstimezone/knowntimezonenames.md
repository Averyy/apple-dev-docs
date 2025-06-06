# knownTimeZoneNames

**Framework**: Foundation  
**Kind**: property

Returns an array of strings listing the IDs of all the time zones known to the system.

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
class var knownTimeZoneNames: [String] { get }
```

#### Return Value

An array of strings listing the IDs of all the time zones known to the system.

#### Discussion

An array of strings listing the IDs of all the time zones known to the system.

## See Also

- [init?(name: String)](nstimezone/init(name:).md)
  Returns a time zone initialized with a given identifier.
- [init?(name: String, data: Data?)](nstimezone/init(name:data:).md)
  Initializes a time zone with a given identifier and time zone data.
- [convenience init?(abbreviation: String)](nstimezone/init(abbreviation:).md)
  Returns the time zone object identified by a given abbreviation.
- [convenience init(forSecondsFromGMT: Int)](nstimezone/init(forsecondsfromgmt:).md)
  Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [class var abbreviationDictionary: [String : String]](nstimezone/abbreviationdictionary.md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/knowntimezonenames)*