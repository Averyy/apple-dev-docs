# ByteCountFormatStyle.Attributed

**Framework**: Foundation  
**Kind**: struct

A format style that converts byte counts into attributed strings.

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
struct Attributed
```

#### Overview

Use the [`attributed`](bytecountformatstyle/attributed-swift.property.md) modifier on a [`ByteCountFormatStyle`](bytecountformatstyle.md) to create a format style of this type.

The attributed strings that this fomat style creates contain attributes from the [`AttributeScopes.FoundationAttributes.NumberFormatAttributes`](attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## Topics

### Formatting a byte count
- [func format(Int64) -> AttributedString](bytecountformatstyle/attributed-swift.struct/format(_:).md)
  Formats a numeric byte count, using this style.
### Customizing style behavior
- [var style: ByteCountFormatStyle.Style](bytecountformatstyle/attributed-swift.struct/style.md)
  The semantic style the format style uses to represent a byte count value.
- [ByteCountFormatStyle.Style](bytecountformatstyle/style-swift.enum.md)
  The semantic style to use when formatting a byte count value.
### Accessing style properties
- [var allowedUnits: ByteCountFormatStyle.Units](bytecountformatstyle/attributed-swift.struct/allowedunits.md)
  The units the format style can use to express the byte count.
- [var spellsOutZero: Bool](bytecountformatstyle/attributed-swift.struct/spellsoutzero.md)
  A Boolean value that indicates whether the format style should spell out zero-byte values as text.
- [var includesActualByteCount: Bool](bytecountformatstyle/attributed-swift.struct/includesactualbytecount.md)
  A Boolean value that indicates whether the format style should include the exact byte count, in addition to expressing it in terms of units.
- [var locale: Locale](bytecountformatstyle/attributed-swift.struct/locale.md)
  The locale to use to format the numeric part of the byte count.
### Modifying style locale
- [func locale(Locale) -> ByteCountFormatStyle.Attributed](bytecountformatstyle/attributed-swift.struct/locale(_:).md)
  Modifies the format style to use the specified locale.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var attributed: ByteCountFormatStyle.Attributed](bytecountformatstyle/attributed-swift.property.md)
  An attributed format style based on the byte count format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/attributed-swift.struct)*