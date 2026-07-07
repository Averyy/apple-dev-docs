# Sample

**Framework**: Evaluations  
**Kind**: associatedtype  
**Required**: Yes

The type of input samples in the evaluation dataset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
associatedtype Sample where Self.Sample == Self.SampleLoader.Sample, Self.Sample.ExpectedValue == Self.Subject.Value
```

## See Also

- [associatedtype SampleLoader : Loader](evaluation/sampleloader.md)
  The type of the sample loader used to provide the evaluation dataset.
- [var dataset: Self.SampleLoader](evaluation/dataset.md)
  The evaluation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/sample)*