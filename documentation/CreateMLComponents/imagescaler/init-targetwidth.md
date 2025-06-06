# init(targetWidth:)

**Framework**: Create ML Components  
**Kind**: init

Creates an image scaler transformer that preserves the aspect ratio.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(targetWidth: Double)
```

#### Discussion

This transformer scales an image to match the `targetWidth` while preserving the aspect ratio.

## Parameters

- `targetWidth`: The target image width. It must be positive.

## See Also

- [init(targetSize: CGSize)](imagescaler/init(targetsize:).md)
  Creates an image scaler transformer. This transformer is used to scale an image to the `targetSize`.
- [init(targetHeight: Double)](imagescaler/init(targetheight:).md)
  Creates an image scaler transformer that preserves the aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagescaler/init(targetwidth:))*