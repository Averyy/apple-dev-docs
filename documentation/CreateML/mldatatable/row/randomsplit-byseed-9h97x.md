# randomSplit(by:seed:)

**Framework**: Create ML  
**Kind**: method

Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 11.0+

## Declaration

```swift
func randomSplit<Feature, Annotation>(by proportion: Double, seed: Int? = nil) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>]) where Annotation : Hashable, Self.Element == AnnotatedFeature<Feature, Annotation>
```

#### Return Value

A tuple of arrays.

## Parameters

- `proportion`: A proportion in the range  .
- `seed`: A seed number for a random-number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/randomsplit(by:seed:)-9h97x)*