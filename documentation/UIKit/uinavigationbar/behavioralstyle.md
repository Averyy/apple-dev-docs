# behavioralStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The behavioral style of the navigation bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var behavioralStyle: UIBehavioralStyle { get }
```

```objc
@property (nonatomic, assign, readonly) UIBehavioralStyle behavioralStyle;
```

## Mentions

- [Building a desktop-class iPad app](../building-a-desktop-class-ipad-app.md)

#### Discussion

Use this property to determine the actual behavior style when the [`preferredBehavioralStyle`](./preferredbehavioralstyle.md) is [`UIBehavioralStyle.automatic`](../uibehavioralstyle/automatic.md).

When the value of this property is [`UIBehavioralStyle.mac`](../uibehavioralstyle/mac.md), [`NSToolbar`](../../AppKit/nstoolbar.md) displays the navigation bar’s content when you build your app with Mac Catalyst. Not every navigation item property is supported in every toolbar section. For more information, see [Display content in a toolbar on Mac](../uinavigationitem/title.md#Display-content-in-a-toolbar-on-Mac).

## See Also

### Building with Mac Catalyst
- [var preferredBehavioralStyle: UIBehavioralStyle](./preferredbehavioralstyle.md)
  The preferred behavioral style of the navigation bar.
- [var currentNSToolbarSection: UINavigationBar.NSToolbarSection](./currentnstoolbarsection.md)
  The toolbar section that the navigation bar is currently using.
- [UINavigationBar.NSToolbarSection](./nstoolbarsection.md)
  Constants that determine how the system hosts the navigation bar in an AppKit toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/behavioralstyle)*