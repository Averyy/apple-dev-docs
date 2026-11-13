# init(_:featuresColumnID:annotationsColumnID:)

**Framework**: TabularData  
**Kind**: init  
**Role**: Initializer

Creates a data frame from a sequence of annotated features.

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
init<S, Feature, Annotation>(_ sequence: S, featuresColumnID: ColumnID<Feature>, annotationsColumnID: ColumnID<Annotation>) throws where S : Sequence, S.Element == AnnotatedFeature<Feature, Annotation>
```

## Discussion

- Parameters

  - featuresColumnID: The features column ID in the data frame.
  - annotationsColumnID: The annotations column ID in the data frame.

## See Also

### Working with annotated features
- [func loadRangedAnnotations<Annotation>(parameters: DataFrameTemporalAnnotationParameters<Annotation>, continueOnFailure: Bool) throws -> [AnnotatedFeature<TemporalFileSegment, Annotation>]](./loadrangedannotations%28parameters,continueonfailure%29.md)
  Loads training examples from a data frame containing annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/init(_:featurescolumnid:annotationscolumnid:))*