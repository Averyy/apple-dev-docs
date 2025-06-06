# NSExtensionServiceTouchBarBezelColorName

**Framework**: Bundle Resources  
**Kind**: typealias

The color to use for the bezel around the extension when it appears as a Quick Action in the Touch Bar.

**Availability**:
- macOS 10.14+

#### Discussion

This key is used in conjunction with the [`NSExtensionServiceAllowsTouchBarItem`](information-property-list/nsextension/nsextensionattributes/nsextensionserviceallowstouchbaritem.md) key.

Set the [`NSExtensionServiceTouchBarBezelColorName`](information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbarbezelcolorname.md) key’s value to the name of a color that exists in your extension’s asset catalog—a color that matches a system color is recommended. If no color is specified, a default color is used.

## See Also

- [class NSColor](../AppKit/NSColor.md)
  An object that stores color data and sometimes opacity (alpha value).
- [Standard Colors](../AppKit/standard-colors.md)
  Retrieve the standard color objects for common colors like red, blue, green, black, white, and more.
- [Color Creation](../AppKit/color-creation.md)
  Load colors from asset catalogs, and create colors from raw component values, such as those used by grayscale, RGB, HSB, and CMYK colors.
- [NSExtensionServiceAllowsTouchBarItem](information-property-list/nsextension/nsextensionattributes/nsextensionserviceallowstouchbaritem.md)
  A Boolean value indicating whether the extension appears as a Quick Action in the Touch Bar.
- [NSExtensionServiceTouchBarIconName](information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbariconname.md)
  The name of an icon for display when the extension appears as a Quick Action in the Touch Bar
- [NSExtensionServiceTouchBarLabel](information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbarlabel.md)
  A name for display when the extension appears as a Quick Action in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes/nsextensionservicetouchbarbezelcolorname)*