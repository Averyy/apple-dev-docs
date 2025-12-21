# parse(_:)

**Framework**: Foundation  
**Kind**: method

Returns a `Date` of a given string interpreted using the current settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func parse(_ value: String) throws -> Date
```

#### Return Value

A `Date` represented by `value`.

#### Discussion

> **Note**: Throws `NSFormattingError` if the string cannot be parsed.

## Parameters

- `value`: A string representation of a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/parsestrategy/parse(_:))*