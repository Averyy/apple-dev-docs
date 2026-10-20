# summary()

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Generates a categorical summary of the filled column’s elements, including default values.

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
func summary() -> CategoricalSummary<FilledColumn<Base>.WrappedElement>
```

Available when `Base` conforms to `OptionalColumnProtocol` and `Base.WrappedElement` conforms to `Hashable`.

## See Also

### Summarizing a Column
- [func numericSummary() -> NumericSummary<Double>](./numericsummary%28%29-3ao8s.md)
  Generates a numeric summary of the integer column’s elements.
- [func numericSummary() -> NumericSummary<Base.WrappedElement>](./numericsummary%28%29-86mgh.md)
  Generates a numeric summary of the floating-point column’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn/summary())*