# MLObjectDetector.ObjectAnnotation

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

The label, location, and confidence score of an item the object detector found in an image.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ObjectAnnotation
```

## Topics

### Creating an annotation
- [init(label: String, boundingBox: CGRect, confidence: Double)](./objectannotation/init%28label,boundingbox,confidence%29.md)
  Creates an annotation for an item an object detector finds in an image.
### Inspecting an annotation
- [var label: String](./objectannotation/label.md)
  The name of the item the object detector found in an image.
- [var boundingBox: CGRect](./objectannotation/boundingbox.md)
  A rectangular region that encloses an item the object detector found in the image.
- [var confidence: Double](./objectannotation/confidence.md)
  The object detector’s confidence score for its prediction’s accuracy.
### Describing an annotation
- [var description: String](./objectannotation/description.md)
  A text representation of the object annotation.
- [var debugDescription: String](./objectannotation/debugdescription.md)
  A text representation of the object annotation that’s suitable for output during debugging.
- [var playgroundDescription: Any](./objectannotation/playgrounddescription.md)
  A description of the object annotation within a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./objectannotation/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./objectannotation/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./objectannotation/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Testing an object detector
- [func prediction(from: URL) throws -> MLObjectDetector.DetectedObjects](./prediction%28from%29.md)
  Locates objects in an image and generates an annotation for each object it detects.
- [func predictions(from: [URL]) throws -> [MLObjectDetector.DetectedObjects]](./predictions%28from%29.md)
  Locates objects in an array of images and generates an array of annotation collections, one for each input image.
- [MLObjectDetector.DetectedObjects](./detectedobjects.md)
  An array of annotations that represent the items an object detector found in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/objectannotation)*