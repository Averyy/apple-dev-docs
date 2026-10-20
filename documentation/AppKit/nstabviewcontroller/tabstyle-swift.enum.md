# NSTabViewController.TabStyle

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Tab control style options for a tab view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum TabStyle
```

```c
enum NSTabViewControllerTabStyle : NSInteger;
```

## Topics

### Constants
- [NSTabViewController.TabStyle.segmentedControlOnTop](./tabstyle-swift.enum/segmentedcontrolontop.md)
  A style that displays a segmented control along the top edge of the tab view interface. Access the configuration of the tab items through the tab view, which you can get from the [`tabView`](./tabview.md) property.
- [NSTabViewController.TabStyle.segmentedControlOnBottom](./tabstyle-swift.enum/segmentedcontrolonbottom.md)
  A style that displays a segmented control along the bottom edge of the tab view interface. Access the configuration of the tab items through the tab view, which you can get from the [`tabView`](./tabview.md) property.
- [NSTabViewController.TabStyle.toolbar](./tabstyle-swift.enum/toolbar.md)
  A style that automatically adds any tabs to the window’s toolbar. The tab view controller takes control of the window’s toolbar and sets itself as the toolbar’s delegate. Customization of the toolbar is handled using the methods in Responding to Toolbar Events.
- [NSTabViewController.TabStyle.unspecified](./tabstyle-swift.enum/unspecified.md)
  A style that indicates the tab view controller does not provide the tab selection UI. Your app provides the control (such as an [`NSSegmentedControl`](../nssegmentedcontrol.md) or [`NSPopUpButton`](../nspopupbutton.md)) for navigating between tabs. You can bind an existing control to the tab view controller object so that interactions with the control automatically change tabs.
### Initializers
- [init?(rawValue: Int)](./tabstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewcontroller/tabstyle-swift.enum)*