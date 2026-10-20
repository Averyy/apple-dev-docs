# numericSummary()

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a numeric summary of the integer column’s elements.

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
func numericSummary() -> NumericSummary<Double>
```

Available when `Base` conforms to `OptionalColumnProtocol` and `Base.WrappedElement` conforms to `BinaryInteger`.

## See Also

### Summarizing a Column
- [func summary() -> CategoricalSummary<FilledColumn<Base>.WrappedElement>](./summary%28%29.md)
  Generates a categorical summary of the filled column’s elements, including default values.
- [func numericSummary() -> NumericSummary<Base.WrappedElement>](./numericsummary%28%29-86mgh.md)
  Generates a numeric summary of the floating-point column’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/numericsummary()-3ao8s)*