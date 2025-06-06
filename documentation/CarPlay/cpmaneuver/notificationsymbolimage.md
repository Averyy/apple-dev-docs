# notificationSymbolImage

**Framework**: CarPlay  
**Kind**: property

An image for notification banners that represents the maneuver.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var notificationSymbolImage: UIImage? { get set }
```

#### Discussion

You use a named image asset to supply variants for both dark and light interface styles, and initialize the image using [`init(named:)`](https://developer.apple.com/documentation/UIKit/UIImage/init(named:)). CarPlay then selects the correct image for the current interface style.

If you don’t provide a notification symbol image, CarPlay uses [`symbolImage`](cpmaneuver/symbolimage.md).

## See Also

- [var symbolImage: UIImage?](cpmaneuver/symbolimage.md)
  An image that represents the maneuver.
- [var dashboardSymbolImage: UIImage?](cpmaneuver/dashboardsymbolimage.md)
  An image for the CarPlay dashboard that represents the maneuver.
- [var symbolSet: CPImageSet?](cpmaneuver/symbolset.md)
  An image set that represents the maneuver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/notificationsymbolimage)*