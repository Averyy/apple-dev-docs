# MLObjectDetector.ObjectAnnotation

**Framework**: Create ML  
**Kind**: struct

The label, location, and confidence score of an item the object detector found in an image.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ObjectAnnotation
```

## Topics

### Creating an annotation
- [init(label: String, boundingBox: CGRect, confidence: Double)](mlobjectdetector/objectannotation/init(label:boundingbox:confidence:).md)
  Creates an annotation for an item an object detector finds in an image.
### Inspecting an annotation
- [var label: String](mlobjectdetector/objectannotation/label.md)
  The name of the item the object detector found in an image.
- [var boundingBox: CGRect](mlobjectdetector/objectannotation/boundingbox.md)
  A rectangular region that encloses an item the object detector found in the image.
- [var confidence: Double](mlobjectdetector/objectannotation/confidence.md)
  The object detector’s confidence score for its prediction’s accuracy.
### Describing an annotation
- [var description: String](mlobjectdetector/objectannotation/description.md)
  A text representation of the object annotation.
- [var debugDescription: String](mlobjectdetector/objectannotation/debugdescription.md)
  A text representation of the object annotation that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlobjectdetector/objectannotation/playgrounddescription.md)
  A description of the object annotation within a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlobjectdetector/objectannotation/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlobjectdetector/objectannotation/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlobjectdetector/objectannotation/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func prediction(from: URL) throws -> MLObjectDetector.DetectedObjects](mlobjectdetector/prediction(from:).md)
  Locates objects in an image and generates an annotation for each object it detects.
- [func predictions(from: [URL]) throws -> [MLObjectDetector.DetectedObjects]](mlobjectdetector/predictions(from:).md)
  Locates objects in an array of images and generates an array of annotation collections, one for each input image.
- [MLObjectDetector.DetectedObjects](mlobjectdetector/detectedobjects.md)
  An array of annotations that represent the items an object detector found in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/objectannotation)*