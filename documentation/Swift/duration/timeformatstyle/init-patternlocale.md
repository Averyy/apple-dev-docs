# init(pattern:locale:)

**Framework**: Swift  
**Kind**: init

Creates a time format style using the provided pattern and optional locale.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(pattern: Duration.TimeFormatStyle.Pattern, locale: Locale = .autoupdatingCurrent)
```

## Parameters

- `pattern`: A   that specifies the units to include in the displayed string and the behavior of the units.
- `locale`: The   used to create the string representation of the duration. This parameter defaults to  .

## See Also

- [Duration.TimeFormatStyle.Pattern](duration/timeformatstyle/pattern-swift.struct.md)
  The units — including hours, minutes, or seconds — and the configuration of those units, used to format a duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/timeformatstyle/init(pattern:locale:))*