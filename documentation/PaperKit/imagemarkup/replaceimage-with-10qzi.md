# replaceImage(with:)

**Framework**: PaperKit  
**Kind**: method

Replaces the contents of this image markup with an image file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func replaceImage(with url: URL) throws
```

#### Discussion

> **Note**: An error if the image file cannot be loaded or is in an unsupported format.

Image content is shown scaled to fill.

## Parameters

- `url`: The URL of the image file to load and display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/imagemarkup/replaceimage(with:)-10qzi)*