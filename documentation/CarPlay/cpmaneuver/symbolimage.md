# symbolImage

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An image that represents the maneuver.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var symbolImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * symbolImage;
```

#### Discussion

You use a named image asset to supply variants for both dark and light interface styles, and initialize the image using [`init(named:)`](../../UIKit/uiimage/init%28named%29.md). CarPlay then selects the correct image for the current interface style.

## See Also

### Providing symbol images
- [var dashboardSymbolImage: UIImage?](./dashboardsymbolimage.md)
  An image for the CarPlay dashboard that represents the maneuver.
- [var notificationSymbolImage: UIImage?](./notificationsymbolimage.md)
  An image for notification banners that represents the maneuver.
- [var symbolSet: CPImageSet?](./symbolset.md)
  An image set that represents the maneuver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/symbolimage)*