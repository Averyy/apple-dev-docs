# ObjectDetectionAnnotation

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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

### Getting the properties
- [let imageFileName: String](./objectdetectionannotation/imagefilename.md)
  The name of the image file.
- [let objects: [ObjectDetectionAnnotation<Label>.Annotation]](./objectdetectionannotation/objects.md)
  The list of object annotations in the image.
- [ObjectDetectionAnnotation.Annotation](./objectdetectionannotation/annotation.md)
  The annotation represented by an object label and its bounding box.
- [let prominentObject: Label](./objectdetectionannotation/prominentobject.md)
  The most prominent object in the image.
### Encoding and decoding
- [ObjectDetectionAnnotation.CodingKeys](./objectdetectionannotation/codingkeys.md)
  Coding keys for object detection annotations
### Default Implementations
- [Identifiable Implementations](./objectdetectionannotation/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Object detection components
- [struct DetectedObject](./detectedobject.md)
  An item in a detection result.
- [struct ObjectDetectionMetrics](./objectdetectionmetrics.md)
  Metrics for object detection model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionannotation)*