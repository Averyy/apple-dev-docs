# navigationBarNSToolbarSection(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate which section of the toolbar to host the navigation bar in.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func navigationBarNSToolbarSection(_ navigationBar: UINavigationBar) -> UINavigationBar.NSToolbarSection
```

#### Return Value

An [`NSToolbar`](https://developer.apple.com/documentation/AppKit/NSToolbar) section that determines which section to place the navigation bar in, and how to present the navigation bar in that section. Return [`UINavigationBar.NSToolbarSection.none`](uinavigationbar/nstoolbarsection/none.md) to disable [`NSToolbar`](https://developer.apple.com/documentation/AppKit/NSToolbar) hosting, which is equivalent to setting [`preferredBehavioralStyle`](uinavigationbar/preferredbehavioralstyle.md) to [`UIBehavioralStyle.pad`](uibehavioralstyle/pad.md).

#### Discussion

The system calls this method to determine how to render your [`UINavigationBar`](uinavigationbar.md) when you build your app with Mac Catalyst.

## Parameters

- `navigationBar`: The navigation bar to host in an  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbardelegate/navigationbarnstoolbarsection(_:))*