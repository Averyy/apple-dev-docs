# init(scale:aspectRatio:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

Creates an augmentation that crops an input image at a random location with a scale that indicates the lower and upper bounds to randomly scale the height and width of the image. The range must be between 0 and 1.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(scale: ClosedRange<Double>, aspectRatio: Double? = nil)
```

## Parameters

- `scale`: A range of scales.
- `aspectRatio`: A size that specifies the ratio of width to height to use for the cropping rectangle.

## See Also

### Creating an image cropper
- [init(targetSize: CGSize)](./init%28targetsize%29.md)
  Creates an augmentation that crops an input image at a random location to the specified target size.
- [init(targetWidth: Double, targetHeight: Double)](./init%28targetwidth,targetheight%29.md)
  Creates an augmentation that crops an input image at a random location to the specified target width and height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/randomimagecropper/init(scale:aspectratio:))*