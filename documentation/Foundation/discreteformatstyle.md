# DiscreteFormatStyle

**Framework**: Foundation  
**Kind**: protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
protocol DiscreteFormatStyle<FormatInput, FormatOutput> : FormatStyle
```

## Topics

### Instance Methods
- [func discreteInput(after: Self.FormatInput) -> Self.FormatInput?](discreteformatstyle/discreteinput(after:).md)
- [func discreteInput(before: Self.FormatInput) -> Self.FormatInput?](discreteformatstyle/discreteinput(before:).md)
- [func input(after: Self.FormatInput) -> Self.FormatInput?](discreteformatstyle/input(after:).md)
- [func input(before: Self.FormatInput) -> Self.FormatInput?](discreteformatstyle/input(before:).md)

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
### Conforming Types
- [Date.AnchoredRelativeFormatStyle](date/anchoredrelativeformatstyle.md)
- [Date.ComponentsFormatStyle](date/componentsformatstyle.md)
- [Date.FormatStyle](date/formatstyle.md)
- [Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct.md)
- [Date.VerbatimFormatStyle](date/verbatimformatstyle.md)
- [Date.VerbatimFormatStyle.Attributed](date/verbatimformatstyle/attributed-swift.struct.md)

## See Also

- [protocol NSKeyValueObservingCustomization](nskeyvalueobservingcustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discreteformatstyle)*