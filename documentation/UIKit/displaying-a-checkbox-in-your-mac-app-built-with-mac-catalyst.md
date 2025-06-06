# Displaying a checkbox in your Mac app built with Mac Catalyst

**Framework**: UIKit

Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.

#### Overview

A Mac app built with Mac Catalyst that uses the Mac user interface idiom displays a [`UISwitch`](uiswitch.md) as a checkbox when the [`preferredStyle`](uiswitch/preferredstyle.md) value is [`UISwitch.Style.automatic`](uiswitch/style-swift.enum/automatic.md) (the default value) or [`UISwitch.Style.checkbox`](uiswitch/style-swift.enum/checkbox.md). If your app doesn’t use the [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md) idiom, the switch appears as a slider switch. To learn more, see [`Choosing a user interface idiom for your Mac app`](choosing-a-user-interface-idiom-for-your-mac-app.md).

##### Add Text to the Checkbox

To display text alongside the checkbox, set the [`title`](uiswitch/title.md) property.

```swift
let showFavoritesAtTop = UISwitch()
showFavoritesAtTop.title = "Always show favorite recipes at the top"
```

##### Resize the Checkbox

A checkbox-style switch has a default frame size of zero. If you’re not using Auto Layout to determine the size and position of the switch, call [`sizeToFit()`](uiview/sizetofit().md) to resize it so that it uses the appropriate amount of space needed to display the checkbox and its title.

## See Also

- [UIKit Catalog: Creating and customizing views and controls](uikit-catalog-creating-and-customizing-views-and-controls.md)
  Customize your app’s user interface with views and controls.
- [Building and improving your app with Mac Catalyst](building-and-improving-your-app-with-mac-catalyst.md)
  Improve your iPadOS app with Mac Catalyst by supporting native controls, multiple windows, sharing, printing, menus and keyboard shortcuts.
- [Removing the title bar in your Mac app built with Mac Catalyst](removing-the-title-bar-in-your-mac-app-built-with-mac-catalyst.md)
  Display content that fills the entire height of a window by removing the title bar.
- [Toolbar](toolbar.md)
  Provide a space for controls under a window’s title bar and above your custom content.
- [Touch Bar](../AppKit/touch-bar.md)
  Display interactive content and controls in the Touch Bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst)*