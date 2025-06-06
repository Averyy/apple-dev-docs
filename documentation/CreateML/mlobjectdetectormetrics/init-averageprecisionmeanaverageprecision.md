# init(averagePrecision:meanAveragePrecision:)

**Framework**: Create ML  
**Kind**: init

Creates metrics for an object detector given an average precision and a mean average precision.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(averagePrecision: (variedIoU: [String : Double], IoU50: [String : Double]), meanAveragePrecision: (variedIoU: Double, IoU50: Double))
```

#### Discussion

You do not use this initializer. Create ML uses this initializer to generate metrics for you when train an object detector or when you use an evaluation method.

## Parameters

- `averagePrecision`: The   for this  .
- `meanAveragePrecision`: The   for this  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/init(averageprecision:meanaverageprecision:))*