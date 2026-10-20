# bucketEnumerator

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

An enumerator for the buckets containing the data in the histogram.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`buckets`](../histogram/buckets.md) instead.

## Declaration

```swift
var bucketEnumerator: NSEnumerator { get }
```

```objc
@property (strong, readonly, nonnull) NSEnumerator<MXHistogramBucket<NSUnit *> *> * bucketEnumerator;
```

## See Also

### Reading the buckets
- [var totalBucketCount: Int](./totalbucketcount.md)
  The total number of buckets in the histogram.
- [class MXHistogramBucket](../mxhistogrambucket.md)
  An object representing a bucket of data in a histogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxhistogram/bucketenumerator)*