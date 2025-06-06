# attributed

**Framework**: Foundation  
**Kind**: property

An attributed format style based on the byte count format style.

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
var attributed: Measurement<UnitInformationStorage>.AttributedStyle.ByteCount { get }
```

#### Discussion

Use this modifier to create a [`ByteCountFormatStyle.Attributed`](bytecountformatstyle/attributed-swift.struct.md) instance, which formats values as [`AttributedString`](attributedstring.md) instances. These attributed strings contain attributes from the [`AttributeScopes.FoundationAttributes.NumberFormatAttributes`](attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## See Also

- [Measurement.AttributedStyle.ByteCount](measurement/attributedstyle/bytecount.md)
  A format style that converts byte counts into attributed strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount/attributed)*