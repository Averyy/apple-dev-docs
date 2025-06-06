# behavioralStyle

**Framework**: UIKit  
**Kind**: property

The behavioral style of the navigation bar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var behavioralStyle: UIBehavioralStyle { get }
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Discussion

Use this property to determine the actual behavior style when the [`preferredBehavioralStyle`](uinavigationbar/preferredbehavioralstyle.md) is [`UIBehavioralStyle.automatic`](uibehavioralstyle/automatic.md).

When the value of this property is [`UIBehavioralStyle.mac`](uibehavioralstyle/mac.md), [`NSToolbar`](https://developer.apple.com/documentation/AppKit/NSToolbar) hosts the navigation bar’s content when you build your app with Mac Catalyst.

## See Also

- [var preferredBehavioralStyle: UIBehavioralStyle](uinavigationbar/preferredbehavioralstyle.md)
  The preferred behavioral style of the navigation bar.
- [var currentNSToolbarSection: UINavigationBar.NSToolbarSection](uinavigationbar/currentnstoolbarsection.md)
  The toolbar section that the navigation bar is currently using.
- [UINavigationBar.NSToolbarSection](uinavigationbar/nstoolbarsection.md)
  Constants that determine how the system hosts the navigation bar in an AppKit toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/behavioralstyle)*