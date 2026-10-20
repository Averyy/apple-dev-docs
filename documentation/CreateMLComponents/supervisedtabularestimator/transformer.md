# Transformer

**Framework**: Create ML Components  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The transformer type created by this estimator.

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
associatedtype Transformer : TabularTransformer
```

## See Also

### Reading and writing
- [func read(from: URL) throws -> Self.Transformer](./read%28from%29.md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](./write%28_,to,overwrite%29.md)
  Writes the encoded transformer to a file.
- [associatedtype Annotation](./annotation.md)
  The annotation type.
- [var annotationColumnID: ColumnID<Self.Annotation>](./annotationcolumnid.md)
  The annotation column identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtabularestimator/transformer)*