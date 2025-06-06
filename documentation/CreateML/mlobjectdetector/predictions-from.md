# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Locates objects in an array of images and generates an array of annotation collections, one for each input image.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func predictions(from images: [URL]) throws -> [MLObjectDetector.DetectedObjects]
```

#### Return Value

An [`MLObjectDetector.DetectedObjects`](mlobjectdetector/detectedobjects.md) array, where each element represents the annotations of the items the object detector found in the corresponding input image.

#### Discussion

- images: An array of URLs for the image files where you want the object detector to look for objects.

## See Also

- [func prediction(from: URL) throws -> MLObjectDetector.DetectedObjects](mlobjectdetector/prediction(from:).md)
  Locates objects in an image and generates an annotation for each object it detects.
- [MLObjectDetector.DetectedObjects](mlobjectdetector/detectedobjects.md)
  An array of annotations that represent the items an object detector found in an image.
- [MLObjectDetector.ObjectAnnotation](mlobjectdetector/objectannotation.md)
  The label, location, and confidence score of an item the object detector found in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/predictions(from:))*