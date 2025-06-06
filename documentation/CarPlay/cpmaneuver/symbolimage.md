# symbolImage

**Framework**: CarPlay  
**Kind**: property

An image that represents the maneuver.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var symbolImage: UIImage? { get set }
```

#### Discussion

You use a named image asset to supply variants for both dark and light interface styles, and initialize the image using [`init(named:)`](https://developer.apple.com/documentation/UIKit/UIImage/init(named:)). CarPlay then selects the correct image for the current interface style.

## See Also

- [var dashboardSymbolImage: UIImage?](cpmaneuver/dashboardsymbolimage.md)
  An image for the CarPlay dashboard that represents the maneuver.
- [var notificationSymbolImage: UIImage?](cpmaneuver/notificationsymbolimage.md)
  An image for notification banners that represents the maneuver.
- [var symbolSet: CPImageSet?](cpmaneuver/symbolset.md)
  An image set that represents the maneuver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuver/symbolimage)*