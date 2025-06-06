# toggleSidebar(_:)

**Framework**: AppKit  
**Kind**: method

Collapses or expands the first sidebar in the split view controller using an animation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@IBAction
@MainActor func toggleSidebar(_ sender: Any?)
```

#### Discussion

If the split view controller doesn’t contain a sidebar, calling this method does nothing.

## See Also

- [var minimumThicknessForInlineSidebars: CGFloat](nssplitviewcontroller/minimumthicknessforinlinesidebars.md)
  The minimum thickness for a sidebar before it automatically collapses.
- [class let automaticDimension: CGFloat](nssplitviewcontroller/automaticdimension.md)
  The default value to apply to a dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/togglesidebar(_:))*