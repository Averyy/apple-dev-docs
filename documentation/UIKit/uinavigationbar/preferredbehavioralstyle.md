# preferredBehavioralStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred behavioral style of the navigation bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var preferredBehavioralStyle: UIBehavioralStyle { get set }
```

```objc
@property (nonatomic, assign, readwrite) UIBehavioralStyle preferredBehavioralStyle;
```

## Mentions

- [Building a desktop-class iPad app](../building-a-desktop-class-ipad-app.md)

#### Discussion

Use this property to specify the behavioral style for the navigation bar. If the value of the property is [`UIBehavioralStyle.automatic`](../uibehavioralstyle/automatic.md), use the [`behavioralStyle`](./behavioralstyle.md) property to determine the actual style.

The default value of this property is [`UIBehavioralStyle.automatic`](../uibehavioralstyle/automatic.md). To learn more about behavioral styles, see [`UIBehavioralStyle`](../uibehavioralstyle.md).

## See Also

### Building with Mac Catalyst
- [var behavioralStyle: UIBehavioralStyle](./behavioralstyle.md)
  The behavioral style of the navigation bar.
- [var currentNSToolbarSection: UINavigationBar.NSToolbarSection](./currentnstoolbarsection.md)
  The toolbar section that the navigation bar is currently using.
- [UINavigationBar.NSToolbarSection](./nstoolbarsection.md)
  Constants that determine how the system hosts the navigation bar in an AppKit toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/preferredbehavioralstyle)*