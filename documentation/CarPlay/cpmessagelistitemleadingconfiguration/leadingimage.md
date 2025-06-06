# leadingImage

**Framework**: CarPlay  
**Kind**: property

The configuration’s image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var leadingImage: UIImage? { get }
```

#### Discussion

Configurations are immutable. To change or remove the image that the message list item’s leading region shows, create a new configuration and update the list item’s [`leadingConfiguration`](cpmessagelistitem/leadingconfiguration.md) property.

A configuration’s image can’t be larger than [`CPMaximumMessageItemImageSize`](cpmaximummessageitemimagesize.md). If you use an animated image, this property returns the first image in the animation sequence.

## See Also

- [var isUnread: Bool](cpmessagelistitemleadingconfiguration/isunread.md)
  A Boolean value that determines whether the message list item displays an unread indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemleadingconfiguration/leadingimage)*