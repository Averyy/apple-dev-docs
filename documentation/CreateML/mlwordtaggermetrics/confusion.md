# confusion

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

A table comparing the actual and predicted labels for each tagging category.

**Availability**:
- macOS 10.14+ - Deprecated in 14.0

## Declaration

```swift
var confusion: MLDataTable { get }
```

## See Also

### Analyzing the tagger’s performance
- [var taggingError: Double](./taggingerror.md)
  The fraction of incorrectly tagged examples.
- [var precisionRecall: MLDataTable](./precisionrecall.md)
  A data table listing the precision and recall percentages for each category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/confusion)*