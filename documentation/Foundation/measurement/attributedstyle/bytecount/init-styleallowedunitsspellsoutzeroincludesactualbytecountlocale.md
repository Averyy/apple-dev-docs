# init(style:allowedUnits:spellsOutZero:includesActualByteCount:locale:)

**Framework**: Foundation  
**Kind**: init

Initializes an attributed byte count format style.

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
init(style: Measurement<UnitType>.AttributedStyle.ByteCount.Style, allowedUnits: Measurement<UnitType>.AttributedStyle.ByteCount.Units, spellsOutZero: Bool, includesActualByteCount: Bool, locale: Locale)
```

## Parameters

- `style`: The style of byte count to express, such as memory or file system storage.
- `allowedUnits`: The units the format style can use to express the byte count.
- `spellsOutZero`: A Boolean value that indicates whether the format style should spell out zero-byte values as text, like  .
- `includesActualByteCount`: A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units. For example,  .
- `locale`: The locale to use to format the numeric part of the byte count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount/init(style:allowedunits:spellsoutzero:includesactualbytecount:locale:))*