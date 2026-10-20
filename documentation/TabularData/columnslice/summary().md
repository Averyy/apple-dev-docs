# summary()

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a categorical summary of the column slice’s elements.

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
func summary() -> CategoricalSummary<WrappedElement>
```

Available when `WrappedElement` conforms to `Hashable`.

## See Also

### Summarizing a Column Slice
- [func numericSummary() -> NumericSummary<Double>](./numericsummary%28%29-68ohj.md)
  Generates a numeric summary of the integer column slice’s elements.
- [func numericSummary() -> NumericSummary<WrappedElement>](./numericsummary%28%29-5swa5.md)
  Generates a numeric summary of the floating-point column slice’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/summary())*