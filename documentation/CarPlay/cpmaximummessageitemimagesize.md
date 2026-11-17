# CPMaximumMessageItemImageSize

**Framework**: CarPlay  
**Kind**: var  
**Role**: Global Variable

The maximum size for images in the leading and trailing regions of a message list item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
let CPMaximumMessageItemImageSize: CGSize
```

```c
extern const CGSize CPMaximumMessageItemImageSize;
```

## Discussion

This constant contains the maximum size for custom images you use with the [`CPMessageListItemLeadingConfiguration`](./cpmessagelistitemleadingconfiguration.md) and [`CPMessageListItemTrailingConfiguration`](./cpmessagelistitemtrailingconfiguration.md) types. The size values are in points. To get the pixel values, multiply this constant by the scale factor in the current traits collection for the vehicle, which you can get from the current [`CPInterfaceController`](./cpinterfacecontroller.md) object.

## See Also

### List items
- [class CPMessageListItem](./cpmessagelistitem.md)
  A list template row that manages a text message thread or contact.
- [class CPMessageListItemLeadingConfiguration](./cpmessagelistitemleadingconfiguration.md)
  A type that defines the content at the leading edge of a message list item’s row.
- [class CPMessageListItemTrailingConfiguration](./cpmessagelistitemtrailingconfiguration.md)
  A type that defines the content at the trailing edge of a message list item’s row.
- [let CPMaximumMessageItemLeadingDetailTextImageSize: CGSize](./cpmaximummessageitemleadingdetailtextimagesize.md)
  The maximum size for images in the detail text image of a message list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaximummessageitemimagesize)*