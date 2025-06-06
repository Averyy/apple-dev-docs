# randomSplit(by:using:)

**Framework**: Create ML  
**Kind**: method

Generates two AnnotatedFeatures by randomly splitting the elements of the sequence, at the same proportion within each unique Annotation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func randomSplit<Feature, Annotation, Generator>(by proportion: Double, using generator: inout Generator) -> ([AnnotatedFeature<Feature, Annotation>], [AnnotatedFeature<Feature, Annotation>]) where Annotation : Hashable, Generator : RandomNumberGenerator, Self.Element == AnnotatedFeature<Feature, Annotation>
```

#### Return Value

A tuple of arrays.

## Parameters

- `proportion`: A proportion in the range  .
- `generator`: A random-number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/randomsplit(by:using:)-4pyzb)*