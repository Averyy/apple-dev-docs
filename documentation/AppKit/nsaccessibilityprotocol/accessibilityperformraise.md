# accessibilityPerformRaise()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Brings the window to the front.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformRaise() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

The window behaves as if you had clicked on the window’s title bar.

## See Also

- [func accessibilityPerformShowAlternateUI() -> Bool](nsaccessibilityprotocol/accessibilityperformshowalternateui.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowDefaultUI() -> Bool](nsaccessibilityprotocol/accessibilityperformshowdefaultui.md)
  Returns to the accessibility element’s original UI.
- [func accessibilityPerformShowMenu() -> Bool](nsaccessibilityprotocol/accessibilityperformshowmenu.md)
  Displays the menu accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformraise())*