# toggleSidebar(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Collapses or expands the first sidebar in the split view controller using an animation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@IBAction
func toggleSidebar(_ sender: Any?)
```

```objc
- (void) toggleSidebar:(id) sender;
```

#### Discussion

If the split view controller doesn’t contain a sidebar, calling this method does nothing.

## See Also

### Managing Sidebars
- [var minimumThicknessForInlineSidebars: CGFloat](./minimumthicknessforinlinesidebars.md)
  The minimum thickness for a sidebar before it automatically collapses.
- [class let automaticDimension: CGFloat](./automaticdimension.md)
  The default value to apply to a dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/togglesidebar(_:))*