# visible

**Framework**: SwiftUI  
**Kind**: property

Prefer to show window toolbar when the window is in full screen mode.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let visible: WindowToolbarFullScreenVisibility
```

#### Discussion

This has no effect if the toolbar is completely hidden, i.e. setting the visibility to `hidden` for `windowToolbar` placements using [`toolbarVisibility(_:for:)`](view/toolbarvisibility(_:for:).md) will cause the toolbar to remain completely hidden, even in full screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowtoolbarfullscreenvisibility/visible)*