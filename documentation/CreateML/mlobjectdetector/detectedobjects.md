# MLObjectDetector.DetectedObjects

**Framework**: Create ML  
**Kind**: typealias  
**Role**: Type Alias

An array of annotations that represent the items an object detector found in an image.

**Availability**:
- macOS 10.15+

## Declaration

```swift
typealias DetectedObjects = [MLObjectDetector.ObjectAnnotation]
```

## See Also

### Testing an object detector
- [func prediction(from: URL) throws -> MLObjectDetector.DetectedObjects](./prediction%28from%29.md)
  Locates objects in an image and generates an annotation for each object it detects.
- [func predictions(from: [URL]) throws -> [MLObjectDetector.DetectedObjects]](./predictions%28from%29.md)
  Locates objects in an array of images and generates an array of annotation collections, one for each input image.
- [MLObjectDetector.ObjectAnnotation](./objectannotation.md)
  The label, location, and confidence score of an item the object detector found in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/detectedobjects)*