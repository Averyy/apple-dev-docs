# ObjectDetectionAnnotation.Annotation

**Framework**: Create ML Components  
**Kind**: struct

The annotation represented by an object label and its bounding box.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Annotation
```

## Topics

### Getting the properties
- [let boundingBox: CGRect](objectdetectionannotation/annotation/boundingbox.md)
  The bounding box that describes the spatial location of the object.
- [let label: Label](objectdetectionannotation/annotation/label.md)
  The object label.
### Encoding and decoding
- [ObjectDetectionAnnotation.Annotation.CodingKeys](objectdetectionannotation/annotation/codingkeys.md)
  Coding keys for Annotation.
### Operators
- [static func == (ObjectDetectionAnnotation<Label>.Annotation, ObjectDetectionAnnotation<Label>.Annotation) -> Bool](objectdetectionannotation/annotation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Decodable Implementations](objectdetectionannotation/annotation/decodable-implementations.md)
- [Equatable Implementations](objectdetectionannotation/annotation/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let imageFileName: String](objectdetectionannotation/imagefilename.md)
  The name of the image file.
- [let objects: [ObjectDetectionAnnotation<Label>.Annotation]](objectdetectionannotation/objects.md)
  The list of object annotations in the image.
- [let prominentObject: Label](objectdetectionannotation/prominentobject.md)
  The most prominent object in the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionannotation/annotation)*