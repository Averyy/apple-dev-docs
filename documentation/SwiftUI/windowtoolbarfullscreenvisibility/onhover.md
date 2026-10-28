# onHover

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

Hide the window toolbar in full screen mode by default. It will reveal itself when the mouse moves into the area occupied by the menu bar.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let onHover: WindowToolbarFullScreenVisibility
```

## Discussion

This has no effect if the toolbar is completely hidden, i.e. setting the visibility to `hidden` for `windowToolbar` placements using [`toolbarVisibility(_:for:)`](../view/toolbarvisibility%28_,for%29.md) will cause the toolbar to remain completely hidden, even in full screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowtoolbarfullscreenvisibility/onhover)*