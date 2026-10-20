# bucketCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

An integer representing the number of samples in the bucket.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`count`](../histogram/bucket/count.md) instead.

## Declaration

```swift
var bucketCount: Int { get }
```

```objc
@property (readonly) NSUInteger bucketCount;
```

## See Also

### Reading the Data
- [var bucketStart: Measurement<UnitType>](./bucketstart.md)
  The value of the starting measurement for the bucket.
- [var bucketEnd: Measurement<UnitType>](./bucketend.md)
  The value of the ending measurement for the bucket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxhistogrambucket/bucketcount)*