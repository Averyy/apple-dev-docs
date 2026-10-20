# meanAveragePrecision

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Two mean-average precisions at different thresholds.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var meanAveragePrecision: (variedIoU: Double, IoU50: Double) { get }
```

## Parameters

- `variedIoU`: The mean of the average precision values across all classes at various thresholds, varying from 50% to 95%, of the intersection-over-union metric.
- `IoU50`: The mean of the average precision values across all classes at a 50% threshold of intersection-over-union metric.

## See Also

### Assessing the model
- [var averagePrecision: (variedIoU: [String : Double], IoU50: [String : Double])](./averageprecision.md)
  Two dictionaries of average precisions at different thresholds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/meanaverageprecision)*