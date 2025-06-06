# accessibilityPerformShowMenu()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Displays the menu accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformShowMenu() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Use this method to display the contextual menu for the element.

## See Also

- [func accessibilityPerformShowAlternateUI() -> Bool](nsaccessibilityprotocol/accessibilityperformshowalternateui.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowDefaultUI() -> Bool](nsaccessibilityprotocol/accessibilityperformshowdefaultui.md)
  Returns to the accessibility element’s original UI.
- [func accessibilityPerformRaise() -> Bool](nsaccessibilityprotocol/accessibilityperformraise.md)
  Brings the window to the front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformshowmenu())*