# accessibilityPerformShowDefaultUI()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns to the accessibility element’s original UI.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityPerformShowDefaultUI() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Call this method after successfully calling [`accessibilityPerformShowAlternateUI()`](nsaccessibilitycontainstransientui/accessibilityperformshowalternateui().md) to return to the original UI.

## See Also

- [func accessibilityPerformShowAlternateUI() -> Bool](nsaccessibilitycontainstransientui/accessibilityperformshowalternateui.md)
  Displays the accessibility element’s alternative UI.
- [func isAccessibilityAlternateUIVisible() -> Bool](nsaccessibilitycontainstransientui/isaccessibilityalternateuivisible.md)
  Returns a Boolean value that determines whether the accessibility element’s alternative UI is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui/accessibilityperformshowdefaultui())*