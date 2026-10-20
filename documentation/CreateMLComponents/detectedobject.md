# DetectedObject

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An item in a detection result.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct DetectedObject<Label> where Label : Comparable, Label : Hashable
```

## Topics

### Creating a detected object
- [init(boundingBox: CGRect, label: Label, probability: Float)](./detectedobject/init%28boundingbox,label,probability%29.md)
  Creates a detected object with bounding box, object label and confidence.
### Getting the properties
- [var boundingBox: CGRect](./detectedobject/boundingbox.md)
  The bounding box of the detected object.
- [var confidence: Float](./detectedobject/confidence.md)
  The detection confidence. The value will always be between 0.0 and 1.0.
- [var label: Label](./detectedobject/label.md)
  The detected object label.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Object detection components
- [struct ObjectDetectionAnnotation](./objectdetectionannotation.md)
  An object detection annotation.
- [struct ObjectDetectionMetrics](./objectdetectionmetrics.md)
  Metrics for object detection model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/detectedobject)*