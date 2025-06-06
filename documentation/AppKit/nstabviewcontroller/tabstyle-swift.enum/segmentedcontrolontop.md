# NSTabViewController.TabStyle.segmentedControlOnTop

**Framework**: AppKit  
**Kind**: case

A style that displays a segmented control along the top edge of the tab view interface. Access the configuration of the tab items through the tab view, which you can get from the [`tabView`](nstabviewcontroller/tabview.md) property.

**Availability**:
- macOS 10.10+

## Declaration

```swift
case segmentedControlOnTop
```

## See Also

- [NSTabViewController.TabStyle.segmentedControlOnBottom](nstabviewcontroller/tabstyle-swift.enum/segmentedcontrolonbottom.md)
  A style that displays a segmented control along the bottom edge of the tab view interface. Access the configuration of the tab items through the tab view, which you can get from the [`tabView`](nstabviewcontroller/tabview.md) property.
- [NSTabViewController.TabStyle.toolbar](nstabviewcontroller/tabstyle-swift.enum/toolbar.md)
  A style that automatically adds any tabs to the window’s toolbar. The tab view controller takes control of the window’s toolbar and sets itself as the toolbar’s delegate. Customization of the toolbar is handled using the methods in Responding to Toolbar Events.
- [NSTabViewController.TabStyle.unspecified](nstabviewcontroller/tabstyle-swift.enum/unspecified.md)
  A style that indicates the tab view controller does not provide the tab selection UI. Your app provides the control (such as an [`NSSegmentedControl`](nssegmentedcontrol.md) or [`NSPopUpButton`](nspopupbutton.md)) for navigating between tabs. You can bind an existing control to the tab view controller object so that interactions with the control automatically change tabs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabstyle-swift.enum/segmentedcontrolontop)*