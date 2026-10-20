# showsActivityIndicator

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the button displays an activity indicator instead of an image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
var showsActivityIndicator: Bool { get set }
```

#### Discussion

The button respects the [`imagePlacement`](./imageplacement.md) property when positioning the activity indicator.

## See Also

### Configuring the activity indicator
- [var activityIndicatorColorTransformer: UIConfigurationColorTransformer?](./activityindicatorcolortransformer.md)
  The color transformer for resolving the color of the activity indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/showsactivityindicator)*