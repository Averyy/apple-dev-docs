# applied(to:generator:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Randomly crops an image at a random location of a given size.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func applied(to image: CIImage, generator: inout some RandomNumberGenerator, eventHandler: EventHandler? = nil) async throws -> CIImage
```

#### Return Value

The cropped image.

## Parameters

- `image`: The input image.
- `generator`: A random number generator.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/randomimagecropper/applied(to:generator:eventhandler:))*