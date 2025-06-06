# attributed

**Framework**: Foundation  
**Kind**: property

An attributed format style based on the byte count format style.

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
var attributed: ByteCountFormatStyle.Attributed
```

#### Discussion

Use this modifier to create a [`ByteCountFormatStyle.Attributed`](bytecountformatstyle/attributed-swift.struct.md) instance, which formats values as [`AttributedString`](attributedstring.md) instances. These attributed strings contain attributes from the [`AttributeScopes.FoundationAttributes.NumberFormatAttributes`](attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## See Also

- [ByteCountFormatStyle.Attributed](bytecountformatstyle/attributed-swift.struct.md)
  A format style that converts byte counts into attributed strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/attributed-swift.property)*