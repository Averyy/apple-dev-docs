# totalSampleSize

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The total size in bytes of sample data in the buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var totalSampleSize: Int { get }
```

## Discussion

If a sample buffer doesn’t contain same sizes, the value of this property is `0`.

## See Also

### Inspecting Size Information
- [var numSamples: Int](./numsamples.md)
  The number of media samples the buffer contains.
- [func sampleSizes() throws -> [Int]](./samplesizes%28%29.md)
  Retrieves an array of sample sizes that represents each sample in a sample buffer.
- [func sampleSize(at: Int) -> Int](./samplesize%28at%29.md)
  Returns the size of a sample in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/totalsamplesize)*