# abbreviationDictionary

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, copy) NSDictionary<NSString *,NSString *> * abbreviationDictionary;
```

#### Return Value

A dictionary holding the mappings of time zone abbreviations to time zone names.

#### Discussion

Note that more than one time zone may have the same abbreviation—for example, US/Pacific and Canada/Pacific both use the abbreviation “PST.” In these cases, [`abbreviationDictionary`](./abbreviationdictionary.md) chooses a single name to map the abbreviation to.

## See Also

### Creating Time Zones
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/abbreviationdictionary)*