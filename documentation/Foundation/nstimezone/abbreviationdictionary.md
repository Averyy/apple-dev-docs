# abbreviationDictionary

**Framework**: Foundation  
**Kind**: property

Returns a dictionary holding the mappings of time zone abbreviations to time zone names.

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
class var abbreviationDictionary: [String : String] { get set }
```

#### Return Value

A dictionary holding the mappings of time zone abbreviations to time zone names.

#### Discussion

Note that more than one time zone may have the same abbreviation—for example, US/Pacific and Canada/Pacific both use the abbreviation “PST.” In these cases, [`abbreviationDictionary`](nstimezone/abbreviationdictionary.md) chooses a single name to map the abbreviation to.

## See Also

- [init?(name: String)](nstimezone/init(name:).md)
  Returns a time zone initialized with a given identifier.
- [init?(name: String, data: Data?)](nstimezone/init(name:data:).md)
  Initializes a time zone with a given identifier and time zone data.
- [convenience init?(abbreviation: String)](nstimezone/init(abbreviation:).md)
  Returns the time zone object identified by a given abbreviation.
- [convenience init(forSecondsFromGMT: Int)](nstimezone/init(forsecondsfromgmt:).md)
  Returns a time zone object offset from Greenwich Mean Time by a given number of seconds.
- [class var knownTimeZoneNames: [String]](nstimezone/knowntimezonenames.md)
  Returns an array of strings listing the IDs of all the time zones known to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/abbreviationdictionary)*