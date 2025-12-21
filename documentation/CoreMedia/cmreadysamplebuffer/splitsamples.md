# splitSamples()

**Framework**: Core Media  
**Kind**: method

Split sample buffer into a smaller representation, ideally carrying a single sample per resulting sample buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func splitSamples() -> [CMReadySampleBuffer<Content>]
```

#### Discussion

Each sample buffer in the returned array will have individual samples, referring to the sample data and containing correct timing, size and attachments. Array with a single element is returned if the samples in the sample buffer can not be separated. For example:

- if sample sizes are not present
- samples are non-contiguous (e.g. non-interleaved audio)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/splitsamples())*