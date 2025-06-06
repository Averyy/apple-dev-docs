# init(cropRectangle:)

**Framework**: Create ML Components  
**Kind**: init

Creates an image crop transformer. This transformer is used to crop an image to the `cropRectangle`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(cropRectangle: CGRect)
```

## Parameters

- `cropRectangle`: A crop rectangle to use. It must always be within the input images’ bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagecropper/init(croprectangle:))*