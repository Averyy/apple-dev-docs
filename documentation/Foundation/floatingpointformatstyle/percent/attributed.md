# attributed

**Framework**: Foundation  
**Kind**: property

An attributed format style based on the floating-point percent format style.

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
var attributed: FloatingPointFormatStyle<Value>.Attributed { get }
```

#### Discussion

Use this modifier to create an [`FloatingPointFormatStyle.Attributed`](floatingpointformatstyle/attributed-swift.struct.md) instance, which formats values as [`AttributedString`](attributedstring.md) instances. These attributed strings contain attributes from the [`AttributeScopes.FoundationAttributes.NumberFormatAttributes`](attributescopes/foundationattributes/numberformatattributes.md) attribute scope. Use these attributes to determine which runs of the attributed string represent different parts of the formatted value.

## See Also

- [FloatingPointFormatStyle.Attributed](floatingpointformatstyle/attributed-swift.struct.md)
  A format style that converts integers into attributed strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/floatingpointformatstyle/percent/attributed)*