# baselineOffsetFromBottom

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The position of the baseline relative to the bottom of the image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
@property (nonatomic, readonly) CGFloat baselineOffsetFromBottom;
```

#### Discussion

Positive values place the baseline up inside the image, and negative values place the baseline below the bottom of the image. When the value of this property is `0.0`, the baseline position is equal to the bottom of the image.

## See Also

### Managing the baseline
- [hasBaseline](./hasbaseline.md)
  A Boolean value that indicates whether the image has a defined baseline offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/baselineoffsetfrombottom-23gkf)*