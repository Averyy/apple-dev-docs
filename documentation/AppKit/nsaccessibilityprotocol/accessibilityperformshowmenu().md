# accessibilityPerformShowMenu()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Displays the menu accessibility element.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformShowMenu() -> Bool
```

```objc
- (BOOL) accessibilityPerformShowMenu;
```

#### Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Use this method to display the contextual menu for the element.

## See Also

### Showing user interface elements
- [func accessibilityPerformShowAlternateUI() -> Bool](./accessibilityperformshowalternateui%28%29.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowDefaultUI() -> Bool](./accessibilityperformshowdefaultui%28%29.md)
  Returns to the accessibility element’s original UI.
- [func accessibilityPerformRaise() -> Bool](./accessibilityperformraise%28%29.md)
  Brings the window to the front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformshowmenu())*