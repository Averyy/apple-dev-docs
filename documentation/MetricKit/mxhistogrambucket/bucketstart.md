# bucketStart

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The value of the starting measurement for the bucket.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`lowerBound`](../histogram/bucket/lowerbound.md) instead.

## Declaration

```swift
var bucketStart: Measurement<UnitType> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnit *> * bucketStart;
```

## See Also

### Reading the Data
- [var bucketEnd: Measurement<UnitType>](./bucketend.md)
  The value of the ending measurement for the bucket.
- [var bucketCount: Int](./bucketcount.md)
  An integer representing the number of samples in the bucket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxhistogrambucket/bucketstart)*