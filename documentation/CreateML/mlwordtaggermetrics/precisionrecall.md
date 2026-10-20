# precisionRecall

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

A data table listing the precision and recall percentages for each category.

**Availability**:
- macOS 10.14+ - Deprecated in 14.0

## Declaration

```swift
var precisionRecall: MLDataTable { get }
```

## See Also

### Analyzing the tagger’s performance
- [var taggingError: Double](./taggingerror.md)
  The fraction of incorrectly tagged examples.
- [var confusion: MLDataTable](./confusion.md)
  A table comparing the actual and predicted labels for each tagging category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/precisionrecall)*