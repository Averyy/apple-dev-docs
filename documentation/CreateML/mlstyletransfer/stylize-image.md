# stylize(image:)

**Framework**: Create ML  
**Kind**: method

Applies the style the model learned to an image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func stylize(image: CGImage) throws -> CGImage?
```

#### Return Value

An image of type `CGImage` stylized using style of the model.

#### Discussion

> **Note**: `MLCreateError.generic` if stylization fails.

## Parameters

- `image`: An input image the model applies its style to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/stylize(image:))*