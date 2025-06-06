# sampleSize(at:)

**Framework**: Core Media  
**Kind**: method

Returns the size of a sample in bytes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func sampleSize(at sampleIndex: Int) -> Int
```

#### Return Value

The size of the sample.

#### Discussion

If you specify a sample index that isn’t in the range, the system returns `0`. It also returns `0` if the sample buffer contains no sizes, which occurs if the samples in the buffer are noncontiguous, such as noninterleaved audio, or if the sample buffer contains a [`CVImageBuffer`](https://developer.apple.com/documentation/CoreVideo/cvimagebuffer-q40).

## Parameters

- `sampleIndex`: The index of the sample to query.

## See Also

- [var numSamples: Int](cmsamplebuffer/numsamples.md)
  The number of media samples the buffer contains.
- [func sampleSizes() throws -> [Int]](cmsamplebuffer/samplesizes.md)
  Retrieves an array of sample sizes that represents each sample in a sample buffer.
- [var totalSampleSize: Int](cmsamplebuffer/totalsamplesize.md)
  The total size in bytes of sample data in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/samplesize(at:))*