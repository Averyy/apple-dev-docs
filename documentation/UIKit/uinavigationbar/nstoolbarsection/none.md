# UINavigationBar.NSToolbarSection.none

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A constant that disables hosting the navigation bar in the toolbar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

```c
UINavigationBarNSToolbarSectionNone
```

## Discussion

Use this value to disable [`NSToolbar`](../../../AppKit/nstoolbar.md) hosting. This value is equivalent to setting the [`preferredBehavioralStyle`](../preferredbehavioralstyle.md) of the navigation bar to [`UIBehavioralStyle.pad`](../../uibehavioralstyle/pad.md).

## See Also

### Constants
- [UINavigationBar.NSToolbarSection.sidebar](./sidebar.md)
  A constant that hosts the navigation bar in the toolbar’s sidebar column.
- [UINavigationBar.NSToolbarSection.supplementary](./supplementary.md)
  A constant that hosts the navigation bar in the toolbar’s supplementary column.
- [UINavigationBar.NSToolbarSection.content](./content.md)
  A constant that hosts the navigation bar in the toolbar’s content column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/nstoolbarsection/none)*