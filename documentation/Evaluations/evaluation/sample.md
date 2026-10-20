# Sample

**Framework**: Evaluations  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of input samples in the evaluation dataset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
associatedtype Sample where Self.Sample == Self.SampleLoader.Sample, Self.Sample.ExpectedValue == Self.Subject.Value
```

## See Also

### Providing data
- [associatedtype SampleLoader : Loader](./sampleloader.md)
  The type of the sample loader used to provide the evaluation dataset.
- [var dataset: Self.SampleLoader](./dataset.md)
  The evaluation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/sample)*