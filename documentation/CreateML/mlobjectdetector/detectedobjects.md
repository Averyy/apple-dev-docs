# MLObjectDetector.DetectedObjects

**Framework**: Create ML  
**Kind**: typealias

An array of annotations that represent the items an object detector found in an image.

**Availability**:
- macOS 10.15+

## Declaration

```swift
typealias DetectedObjects = [MLObjectDetector.ObjectAnnotation]
```

## See Also

- [func prediction(from: URL) throws -> MLObjectDetector.DetectedObjects](mlobjectdetector/prediction(from:).md)
  Locates objects in an image and generates an annotation for each object it detects.
- [func predictions(from: [URL]) throws -> [MLObjectDetector.DetectedObjects]](mlobjectdetector/predictions(from:).md)
  Locates objects in an array of images and generates an array of annotation collections, one for each input image.
- [MLObjectDetector.ObjectAnnotation](mlobjectdetector/objectannotation.md)
  The label, location, and confidence score of an item the object detector found in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/detectedobjects)*