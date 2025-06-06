# ObjectDetectionAnnotation

**Framework**: Create ML Components  
**Kind**: struct

An object detection annotation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct ObjectDetectionAnnotation<Label> where Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

#### Overview

The annotation consists of a list of bounding boxes and object labels for each image.

## Topics

### Creating an annotation
- [init(from: any Decoder) throws](objectdetectionannotation/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Getting the properties
- [let imageFileName: String](objectdetectionannotation/imagefilename.md)
  The name of the image file.
- [let objects: [ObjectDetectionAnnotation<Label>.Annotation]](objectdetectionannotation/objects.md)
  The list of object annotations in the image.
- [ObjectDetectionAnnotation.Annotation](objectdetectionannotation/annotation.md)
  The annotation represented by an object label and its bounding box.
- [let prominentObject: Label](objectdetectionannotation/prominentobject.md)
  The most prominent object in the image.
### Encoding and decoding
- [ObjectDetectionAnnotation.CodingKeys](objectdetectionannotation/codingkeys.md)
  Coding keys for object detection annotations
### Operators
- [static func == (ObjectDetectionAnnotation<Label>, ObjectDetectionAnnotation<Label>) -> Bool](objectdetectionannotation/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](objectdetectionannotation/equatable-implementations.md)
- [Identifiable Implementations](objectdetectionannotation/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct DetectedObject](detectedobject.md)
  An item in a detection result.
- [struct ObjectDetectionMetrics](objectdetectionmetrics.md)
  Metrics for object detection model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionannotation)*