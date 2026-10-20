# bucketEnd

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The value of the ending measurement for the bucket.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`upperBound`](../histogram/bucket/upperbound.md) instead.

## Declaration

```swift
var bucketEnd: Measurement<UnitType> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnit *> * bucketEnd;
```

## See Also

### Reading the Data
- [var bucketStart: Measurement<UnitType>](./bucketstart.md)
  The value of the starting measurement for the bucket.
- [var bucketCount: Int](./bucketcount.md)
  An integer representing the number of samples in the bucket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxhistogrambucket/bucketend)*