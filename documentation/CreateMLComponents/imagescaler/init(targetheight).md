# init(targetHeight:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

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
init(targetHeight: Double)
```

## Discussion

This transformer scales an image to match the `targetHeight` while preserving the aspect ratio.

## Parameters

- `targetHeight`: The target image height. It must be positive.

## See Also

### Creating a transformer
- [init(targetSize: CGSize)](./init%28targetsize%29.md)
  Creates an image scaler transformer. This transformer is used to scale an image to the `targetSize`.
- [init(targetWidth: Double)](./init%28targetwidth%29.md)
  Creates an image scaler transformer that preserves the aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagescaler/init(targetheight:))*