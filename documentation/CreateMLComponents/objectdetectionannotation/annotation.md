# ObjectDetectionAnnotation.Annotation

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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
- [let boundingBox: CGRect](./annotation/boundingbox.md)
  The bounding box that describes the spatial location of the object.
- [let label: Label](./annotation/label.md)
  The object label.
### Encoding and decoding
- [ObjectDetectionAnnotation.Annotation.CodingKeys](./annotation/codingkeys.md)
  Coding keys for Annotation.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the properties
- [let imageFileName: String](./imagefilename.md)
  The name of the image file.
- [let objects: [ObjectDetectionAnnotation<Label>.Annotation]](./objects.md)
  The list of object annotations in the image.
- [let prominentObject: Label](./prominentobject.md)
  The most prominent object in the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionannotation/annotation)*