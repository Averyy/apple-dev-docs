# annotationColumnID

**Framework**: Create ML Components  
**Kind**: property  
**Required**: Yes

The annotation column identifier.

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
var annotationColumnID: ColumnID<Self.Annotation> { get set }
```

## See Also

- [func read(from: URL) throws -> Self.Transformer](supervisedtabularestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](supervisedtabularestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.
- [associatedtype Annotation](supervisedtabularestimator/annotation.md)
  The annotation type.
- [associatedtype Transformer : TabularTransformer](supervisedtabularestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtabularestimator/annotationcolumnid)*