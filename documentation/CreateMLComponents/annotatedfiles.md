# AnnotatedFiles

**Framework**: Create ML Components  
**Kind**: struct

An annotated files collection.

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
struct AnnotatedFiles
```

## Topics

### Creating the feature
- [init(labeledBySubdirectoryNamesAt: URL, type: UTType, continueOnFailure: Bool) throws](annotatedfiles/init(labeledbysubdirectorynamesat:type:continueonfailure:).md)
  Reads training examples from a directory containing files in labeled sub-directories.
- [init(labeledByNamesAt: URL, separator: Character, index: Int, type: UTType, continueOnFailure: Bool) throws](annotatedfiles/init(labeledbynamesat:separator:index:type:continueonfailure:).md)
  Reads training examples from a directory containing files having their labels in the name. The name can contain multiple words separated by a `separator`. So the `index` tells the position of the label in the file name. Files with incorrect name format are ignored.
### Getting the properties
- [var endIndex: AnnotatedFiles.Index](annotatedfiles/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var startIndex: AnnotatedFiles.Index](annotatedfiles/startindex.md)
  The position of the first element in a nonempty collection.
### Getting the index
- [func index(after: AnnotatedFiles.Index) -> AnnotatedFiles.Index](annotatedfiles/index(after:).md)
  Returns the position immediately after the given index.
- [AnnotatedFiles.Index](annotatedfiles/index.md)
  A type that represents a position in the collection.
- [AnnotatedFiles.Element](annotatedfiles/element.md)
  A type representing the sequence’s elements.
### Accessing by subscript
- [subscript(AnnotatedFiles.Index) -> IndexingIterator<AnnotatedFiles>.Element](annotatedfiles/subscript(_:).md)
  Accesses the element at the specified position.
### Type Aliases
- [AnnotatedFiles.Indices](annotatedfiles/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [AnnotatedFiles.Iterator](annotatedfiles/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [AnnotatedFiles.SubSequence](annotatedfiles/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](annotatedfiles/collection-implementations.md)
- [Decodable Implementations](annotatedfiles/decodable-implementations.md)
- [Encodable Implementations](annotatedfiles/encodable-implementations.md)
- [Equatable Implementations](annotatedfiles/equatable-implementations.md)
- [Hashable Implementations](annotatedfiles/hashable-implementations.md)
- [Sequence Implementations](annotatedfiles/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct AnnotatedBatch](annotatedbatch.md)
  A batch of annotated examples for fitting a supervised estimator.
- [struct AnnotatedFeature](annotatedfeature.md)
  An annotated example for fitting a supervised estimator.
- [struct AnnotatedFeatureProvider](annotatedfeatureprovider.md)
  An adaptor that converts a regular estimator to a tabular estimator by selecting features and annotations from columns.
- [struct AnnotatedPrediction](annotatedprediction.md)
  An annotated prediction.
- [struct DataFrameTemporalAnnotationParameters](dataframetemporalannotationparameters.md)
  Annotation parameters for the dataframe containing temporal annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfiles)*