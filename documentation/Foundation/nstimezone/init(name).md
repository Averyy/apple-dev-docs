# init(name:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithName:(NSString *) tzName;
```

#### Return Value

A time zone object initialized with the identifier `tzName`.

#### Discussion

If `tzName` is a known identifier, this method calls [`init(name:data:)`](./init%28name,data%29.md) with the appropriate data object.

## Parameters

- `tzName`: The identifier for the time zone. Providing `nil` for this parameter raises an invalid argument exception.

## See Also

### Creating Time Zones
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
- [+ timeZoneWithName:](./timezonewithname_.md)
  Returns the time zone object identified by a given identifier.
- [+ timeZoneWithName:data:](./timezonewithname_data_.md)
  Returns the time zone with a given identifier whose data has been initialized using given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/init(name:))*