# accessibilityPerformShowDefaultUI()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns to the accessibility element’s original UI.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityPerformShowDefaultUI() -> Bool
```

```objc
- (BOOL) accessibilityPerformShowDefaultUI;
```

## Return Value

[`true`](../../Swift/true.md) if the action was successfully triggered; otherwise, [`false`](../../Swift/false.md). This method does not indicate the success or failure of the action, just the fact that the action was successfully triggered.

## Discussion

Call this method after successfully calling [`accessibilityPerformShowAlternateUI()`](./accessibilityperformshowalternateui%28%29.md) to return to the original UI.

## See Also

### Supporting Accessibility
- [func accessibilityPerformShowAlternateUI() -> Bool](./accessibilityperformshowalternateui%28%29.md)
  Displays the accessibility element’s alternative UI.
- [func isAccessibilityAlternateUIVisible() -> Bool](./isaccessibilityalternateuivisible%28%29.md)
  Returns a Boolean value that determines whether the accessibility element’s alternative UI is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui/accessibilityperformshowdefaultui())*