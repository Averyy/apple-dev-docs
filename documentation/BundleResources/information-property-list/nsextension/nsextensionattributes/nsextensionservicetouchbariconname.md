# NSExtensionServiceTouchBarIconName

**Framework**: Bundle Resources  
**Kind**: typealias

The name of an icon for display when the extension appears as a Quick Action in the Touch Bar

**Availability**:
- macOS 10.14+

#### Discussion

This key is used in conjunction with the [`NSExtensionServiceAllowsTouchBarItem`](information-property-list/nsextension/nsextensionattributes/nsextensionserviceallowstouchbaritem.md) key.

Set the [`NSExtensionServiceTouchBarIconName`](information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbariconname.md) key’s value to a system icon name or the name of an icon within the extension bundle. This icon should be a : a monochromatic image with transparency, anti-aliasing, and no drop shadow that uses a mask to define its shape. For design guidance, see [`Human Interface Guidelines > macOS > Custom Icons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/icons-and-images/custom-icons/). If no icon is specified, a default icon is used.

## See Also

- [NSExtensionServiceAllowsTouchBarItem](information-property-list/nsextension/nsextensionattributes/nsextensionserviceallowstouchbaritem.md)
  A Boolean value indicating whether the extension appears as a Quick Action in the Touch Bar.
- [NSExtensionServiceTouchBarBezelColorName](information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbarbezelcolorname.md)
  The color to use for the bezel around the extension when it appears as a Quick Action in the Touch Bar.
- [NSExtensionServiceTouchBarLabel](information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbarlabel.md)
  A name for display when the extension appears as a Quick Action in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbariconname)*