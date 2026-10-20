# notificationSymbolImage

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An image for notification banners that represents the maneuver.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var notificationSymbolImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * notificationSymbolImage;
```

#### Discussion

You use a named image asset to supply variants for both dark and light interface styles, and initialize the image using [`init(named:)`](../../UIKit/uiimage/init%28named%29.md). CarPlay then selects the correct image for the current interface style.

If you don’t provide a notification symbol image, CarPlay uses [`symbolImage`](./symbolimage.md).

## See Also

### Providing symbol images
- [var symbolImage: UIImage?](./symbolimage.md)
  An image that represents the maneuver.
- [var dashboardSymbolImage: UIImage?](./dashboardsymbolimage.md)
  An image for the CarPlay dashboard that represents the maneuver.
- [var symbolSet: CPImageSet?](./symbolset.md)
  An image set that represents the maneuver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/notificationsymbolimage)*