# averagePrecision

**Framework**: Create ML  
**Kind**: property

Two dictionaries of average precisions at different thresholds.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var averagePrecision: (variedIoU: [String : Double], IoU50: [String : Double]) { get }
```

## Parameters

- `variedIoU`: The average precision values of all classes at various   thresholds, varying from 50% to 95%, for the intersection-over-union   metric. The keys of the dictionary are each object’s label.
- `IoU50`: The average precision values of all classes at a 50% threshold   of intersection-over-union metric. The keys of the dictionary are each   object’s label.

## See Also

- [var meanAveragePrecision: (variedIoU: Double, IoU50: Double)](mlobjectdetectormetrics/meanaverageprecision.md)
  Two mean-average precisions at different thresholds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/averageprecision)*