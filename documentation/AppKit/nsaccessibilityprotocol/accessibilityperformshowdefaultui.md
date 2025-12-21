# accessibilityPerformShowDefaultUI()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns to the accessibility element’s original UI.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformShowDefaultUI() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Call this method after successfully calling [`accessibilityPerformShowAlternateUI()`](nsaccessibilityprotocol/accessibilityperformshowalternateui().md) to return to the original UI.

## See Also

- [func accessibilityPerformShowAlternateUI() -> Bool](nsaccessibilityprotocol/accessibilityperformshowalternateui.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowMenu() -> Bool](nsaccessibilityprotocol/accessibilityperformshowmenu.md)
  Displays the menu accessibility element.
- [func accessibilityPerformRaise() -> Bool](nsaccessibilityprotocol/accessibilityperformraise.md)
  Brings the window to the front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformshowdefaultui())*