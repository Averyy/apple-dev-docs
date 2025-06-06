# DetectedObject

**Framework**: Create ML Components  
**Kind**: struct

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
- [init(boundingBox: CGRect, label: Label, probability: Float)](detectedobject/init(boundingbox:label:probability:).md)
  Creates a detected object with bounding box, object label and confidence.
### Getting the properties
- [var boundingBox: CGRect](detectedobject/boundingbox.md)
  The bounding box of the detected object.
- [var confidence: Float](detectedobject/confidence.md)
  The detection confidence. The value will always be between 0.0 and 1.0.
- [var label: Label](detectedobject/label.md)
  The detected object label.
### Operators
- [static func == (DetectedObject<Label>, DetectedObject<Label>) -> Bool](detectedobject/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Decodable Implementations](detectedobject/decodable-implementations.md)
- [Encodable Implementations](detectedobject/encodable-implementations.md)
- [Equatable Implementations](detectedobject/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct ObjectDetectionAnnotation](objectdetectionannotation.md)
  An object detection annotation.
- [struct ObjectDetectionMetrics](objectdetectionmetrics.md)
  Metrics for object detection model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/detectedobject)*