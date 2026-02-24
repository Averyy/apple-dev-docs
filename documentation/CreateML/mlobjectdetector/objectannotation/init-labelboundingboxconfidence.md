# init(label:boundingBox:confidence:)

**Framework**: Create ML  
**Kind**: init

Creates an annotation for an item an object detector finds in an image.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(label: String, boundingBox: CGRect, confidence: Double)
```

#### Discussion

Don’t use this initializer to create an object annotation yourself. The object detector uses it to create object annotations when it makes predictions on your images, such as when you use [`prediction(from:)`](mlobjectdetector/prediction(from:).md).

## Parameters

- `label`: The name of the item.
- `boundingBox`: The location of the item in an image.
- `confidence`: The confidence score of the item in the image. The value must be in the range `[0.0, 1.0]`, where `1.0` is the most confident.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/objectannotation/init(label:boundingbox:confidence:))*