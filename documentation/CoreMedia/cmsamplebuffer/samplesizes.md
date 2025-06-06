# sampleSizes()

**Framework**: Core Media  
**Kind**: method

Retrieves an array of sample sizes that represents each sample in a sample buffer.

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
func sampleSizes() throws -> [Int]
```

#### Return Value

An array of sample sizes.

#### Discussion

If the result contains a single element, all samples in the buffer are of this size. If there are no sample sizes in this buffer, the array is empty. This can occur if the samples in the buffer are noncontiguous, like noninterleaved audio, or if the sample buffer contains a [`CVImageBuffer`](https://developer.apple.com/documentation/CoreVideo/cvimagebuffer-q40).

## See Also

- [var numSamples: Int](cmsamplebuffer/numsamples.md)
  The number of media samples the buffer contains.
- [func sampleSize(at: Int) -> Int](cmsamplebuffer/samplesize(at:).md)
  Returns the size of a sample in bytes.
- [var totalSampleSize: Int](cmsamplebuffer/totalsamplesize.md)
  The total size in bytes of sample data in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/samplesizes())*