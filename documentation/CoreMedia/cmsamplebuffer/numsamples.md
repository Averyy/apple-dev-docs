# numSamples

**Framework**: Core Media  
**Kind**: property

The number of media samples the buffer contains.

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
var numSamples: Int { get }
```

#### Discussion

The value is `0` if an error occurs.

## See Also

- [func sampleSizes() throws -> [Int]](cmsamplebuffer/samplesizes.md)
  Retrieves an array of sample sizes that represents each sample in a sample buffer.
- [func sampleSize(at: Int) -> Int](cmsamplebuffer/samplesize(at:).md)
  Returns the size of a sample in bytes.
- [var totalSampleSize: Int](cmsamplebuffer/totalsamplesize.md)
  The total size in bytes of sample data in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/numsamples)*