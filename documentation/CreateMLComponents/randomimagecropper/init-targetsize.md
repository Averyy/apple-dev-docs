# init(targetSize:)

**Framework**: Create ML Components  
**Kind**: init

Creates an augmentation that crops an input image at a random location to the specified target size.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(targetSize: CGSize)
```

## Parameters

- `targetSize`: The target size of the cropping rectangle. Must be positive.

## See Also

- [init(scale: ClosedRange<Double>, aspectRatio: Double?)](randomimagecropper/init(scale:aspectratio:).md)
  Creates an augmentation that crops an input image at a random location with a scale that indicates the lower and upper bounds to randomly scale the height and width of the image. The range must be between 0 and 1.
- [init(targetWidth: Double, targetHeight: Double)](randomimagecropper/init(targetwidth:targetheight:).md)
  Creates an augmentation that crops an input image at a random location to the specified target width and height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/randomimagecropper/init(targetsize:))*