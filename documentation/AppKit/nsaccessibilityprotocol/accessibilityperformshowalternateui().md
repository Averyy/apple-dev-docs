# accessibilityPerformShowAlternateUI()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Displays the accessibility element’s alternative UI.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformShowAlternateUI() -> Bool
```

```objc
- (BOOL) accessibilityPerformShowAlternateUI;
```

#### Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Use this method to trigger changes to the UI due to a mouse-hover or similar event.

## See Also

### Showing user interface elements
- [func accessibilityPerformShowDefaultUI() -> Bool](./accessibilityperformshowdefaultui%28%29.md)
  Returns to the accessibility element’s original UI.
- [func accessibilityPerformShowMenu() -> Bool](./accessibilityperformshowmenu%28%29.md)
  Displays the menu accessibility element.
- [func accessibilityPerformRaise() -> Bool](./accessibilityperformraise%28%29.md)
  Brings the window to the front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformshowalternateui())*