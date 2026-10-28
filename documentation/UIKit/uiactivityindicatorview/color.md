# color

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color of the activity indicator.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var color: UIColor! { get set }
```

```objc
@property (nonatomic, strong, readwrite, null_resettable) UIColor * color;
```

## Discussion

If you set a color for an activity indicator, it overrides the color provided by the [`style`](./style-swift.property.md) property.

## See Also

### Configuring the activity indicator appearance
- [var style: UIActivityIndicatorView.Style](./style-swift.property.md)
  The basic appearance of the activity indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/color)*