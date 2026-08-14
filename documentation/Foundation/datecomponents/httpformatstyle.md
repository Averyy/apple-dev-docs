# DateComponents.HTTPFormatStyle

**Framework**: Foundation  
**Kind**: struct

Converts `DateComponents` into RFC 9110-compatible “HTTP date” `String`, and parses in the reverse direction. This parser does not do validation on the individual values of the components. An optional date can be created from the result using `Calendar(identifier: .gregorian).date(from: ...)`. When formatting, missing or invalid fields are filled with default values: `Sun`, `01`, `Jan`, `2000`, `00:00:00`, `GMT`. Note that missing fields may result in an invalid date or time. Other values in the `DateComponents` are ignored.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct HTTPFormatStyle
```

## Topics

### Initializers
- [init()](datecomponents/httpformatstyle/init.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomConsumingRegexComponent](../swift/customconsumingregexcomponent.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../swift/hashable.md)
- [ParseStrategy](parsestrategy.md)
- [ParseableFormatStyle](parseableformatstyle.md)
- [RegexComponent](../swift/regexcomponent.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/httpformatstyle)*