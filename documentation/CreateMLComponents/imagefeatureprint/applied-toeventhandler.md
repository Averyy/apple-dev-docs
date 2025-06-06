# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Extracts image features from an image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to image: CIImage, eventHandler: EventHandler? = nil) async throws -> MLShapedArray<Float>
```

#### Return Value

A shaped array containing the extracted features of the image.

## Parameters

- `image`: An image.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagefeatureprint/applied(to:eventhandler:))*