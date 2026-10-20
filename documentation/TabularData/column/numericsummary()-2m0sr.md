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

Available when `WrappedElement` conforms to `BinaryInteger`.

## See Also

### Summarizing a Column
- [func summary() -> CategoricalSummary<WrappedElement>](./summary%28%29.md)
  Generates a categorical summary of the column’s elements.
- [func numericSummary() -> NumericSummary<WrappedElement>](./numericsummary%28%29-8laeo.md)
  Generates a numeric summary of the floating-point column’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/numericsummary()-2m0sr)*