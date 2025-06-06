# accessibilityPerformShowAlternateUI()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Displays the accessibility element’s alternative UI.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityPerformShowAlternateUI() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the action was successfully triggered; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

#### Discussion

Use this method to trigger changes to the UI due to a mouse-hover or similar event.

## See Also

- [func accessibilityPerformShowDefaultUI() -> Bool](nsaccessibilitycontainstransientui/accessibilityperformshowdefaultui.md)
  Returns to the accessibility element’s original UI.
- [func isAccessibilityAlternateUIVisible() -> Bool](nsaccessibilitycontainstransientui/isaccessibilityalternateuivisible.md)
  Returns a Boolean value that determines whether the accessibility element’s alternative UI is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui/accessibilityperformshowalternateui())*