# prediction(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Locates objects in an image and generates an annotation for each object it detects.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func prediction(from image: URL) throws -> MLObjectDetector.DetectedObjects
```

## Return Value

An [`MLObjectDetector.DetectedObjects`](./detectedobjects.md) instance — which is an [`MLObjectDetector.ObjectAnnotation`](./objectannotation.md) array — where each annotation represents an item the object detector found in the image.

## Parameters

- `image`: The URL for the image file where you want the object detector to look for objects.

## See Also

### Testing an object detector
- [func predictions(from: [URL]) throws -> [MLObjectDetector.DetectedObjects]](./predictions%28from%29.md)
  Locates objects in an array of images and generates an array of annotation collections, one for each input image.
- [MLObjectDetector.DetectedObjects](./detectedobjects.md)
  An array of annotations that represent the items an object detector found in an image.
- [MLObjectDetector.ObjectAnnotation](./objectannotation.md)
  The label, location, and confidence score of an item the object detector found in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/prediction(from:))*