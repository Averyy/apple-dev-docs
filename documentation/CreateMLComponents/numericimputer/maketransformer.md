# makeTransformer()

**Framework**: Create ML Components  
**Kind**: method

Creates a default-initialized impute transformer suitable for incremental fitting.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func makeTransformer() -> NumericImputer<Element>.Transformer
```

#### Discussion

> **Note**: You can’t use incremental fitting with an impute transformer when using the `median` strategy.

You can’t use incremental fitting with an impute transformer when using the `median` strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/numericimputer/maketransformer())*