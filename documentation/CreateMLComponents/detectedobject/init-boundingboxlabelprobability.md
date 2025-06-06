# init(boundingBox:label:probability:)

**Framework**: Create ML Components  
**Kind**: init

Creates a detected object with bounding box, object label and confidence.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(boundingBox: CGRect, label: Label, probability: Float)
```

## Parameters

- `boundingBox`: The bounding box of the detected object.
- `label`: The label of the detected object.
- `probability`: The detection confidence. The value will always be between 0.0 and 1.0


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/detectedobject/init(boundingbox:label:probability:))*