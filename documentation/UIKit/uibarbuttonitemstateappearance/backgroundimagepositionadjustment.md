# backgroundImagePositionAdjustment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The distance, in points, by which to offset the background image horizontally and vertically.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var backgroundImagePositionAdjustment: UIOffset { get set }
```

```objc
@property (nonatomic, assign, readwrite) UIOffset backgroundImagePositionAdjustment;
```

#### Discussion

Positive values move the image down and to the right. Negative values move the image up and to the left.

## See Also

### Configuring the background appearance
- [var backgroundImage: UIImage?](./backgroundimage.md)
  A background image to display around the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemstateappearance/backgroundimagepositionadjustment)*