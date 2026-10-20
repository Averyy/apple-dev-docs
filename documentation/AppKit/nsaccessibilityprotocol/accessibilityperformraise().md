# accessibilityPerformRaise()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Brings the window to the front.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func accessibilityPerformRaise() -> Bool
```

```objc
- (BOOL) accessibilityPerformRaise;
```

#### Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

The window behaves as if you had clicked on the window’s title bar.

## See Also

### Showing user interface elements
- [func accessibilityPerformShowAlternateUI() -> Bool](./accessibilityperformshowalternateui%28%29.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowDefaultUI() -> Bool](./accessibilityperformshowdefaultui%28%29.md)
  Returns to the accessibility element’s original UI.
- [func accessibilityPerformShowMenu() -> Bool](./accessibilityperformshowmenu%28%29.md)
  Displays the menu accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/accessibilityperformraise())*