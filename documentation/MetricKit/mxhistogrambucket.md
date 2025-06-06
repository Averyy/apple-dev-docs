# MXHistogramBucket

**Framework**: MetricKit  
**Kind**: class

An object representing a bucket of data in a histogram.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXHistogramBucket<UnitType> where UnitType : Unit
```

## Topics

### Reading the Data
- [var bucketStart: Measurement<UnitType>](mxhistogrambucket/bucketstart.md)
  The value of the starting measurement for the bucket.
- [var bucketEnd: Measurement<UnitType>](mxhistogrambucket/bucketend.md)
  The value of the ending measurement for the bucket.
- [var bucketCount: Int](mxhistogrambucket/bucketcount.md)
  An integer representing the number of samples in the bucket.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var bucketEnumerator: NSEnumerator](mxhistogram/bucketenumerator.md)
  An enumerator for the buckets containing the data in the histogram.
- [var totalBucketCount: Int](mxhistogram/totalbucketcount.md)
  The total number of buckets in the histogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxhistogrambucket)*