# init(secondsFromGMT:)

**Framework**: Foundation  
**Kind**: init

Returns a time zone initialized with a specific number of seconds from GMT.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(secondsFromGMT seconds: Int)
```

#### Return Value

A time zone, or `nil` if a valid time zone could not be created from `seconds`.

#### Discussion

Time zones created with this never have daylight savings and the offset is constant no matter the date. The identifier and abbreviation do NOT follow the POSIX convention (of minutes-west).

## Parameters

- `seconds`: The number of seconds from GMT.

## See Also

- [static var knownTimeZoneIdentifiers: [String]](timezone/knowntimezoneidentifiers.md)
  Returns an array of strings listing the identifier of all the time zones known to the system.
- [static var abbreviationDictionary: [String : String]](timezone/abbreviationdictionary.md)
  Returns the mapping of abbreviations to time zone identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timezone/init(secondsfromgmt:))*