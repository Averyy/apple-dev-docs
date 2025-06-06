# init(targetSize:)

**Framework**: Create ML Components  
**Kind**: init

Creates an image scaler transformer. This transformer is used to scale an image to the `targetSize`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(targetSize: CGSize)
```

## Parameters

- `targetSize`: The target image size. Both width and height must be positive.

## See Also

- [init(targetHeight: Double)](imagescaler/init(targetheight:).md)
  Creates an image scaler transformer that preserves the aspect ratio.
- [init(targetWidth: Double)](imagescaler/init(targetwidth:).md)
  Creates an image scaler transformer that preserves the aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagescaler/init(targetsize:))*