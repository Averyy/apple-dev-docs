# confidence

**Framework**: Create ML  
**Kind**: property

The object detector’s confidence score for its prediction’s accuracy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var confidence: Double
```

#### Discussion

The confidence range is `[0.0, 1.0]`, where `1.0` is the highest possible confidence score.

## See Also

- [var label: String](mlobjectdetector/objectannotation/label.md)
  The name of the item the object detector found in an image.
- [var boundingBox: CGRect](mlobjectdetector/objectannotation/boundingbox.md)
  A rectangular region that encloses an item the object detector found in the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/objectannotation/confidence)*