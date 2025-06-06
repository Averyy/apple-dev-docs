# isAccessibilityAlternateUIVisible()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that determines whether the accessibility element’s alternative UI is currently visible.

**Availability**:
- macOS ?+

## Declaration

```swift
func isAccessibilityAlternateUIVisible() -> Bool
```

#### Return Value

Use this property for elements that present an alternate UI—for example, when the pointer hovers over an interface element for a few seconds.

## See Also

- [func accessibilityPerformShowAlternateUI() -> Bool](nsaccessibilitycontainstransientui/accessibilityperformshowalternateui.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowDefaultUI() -> Bool](nsaccessibilitycontainstransientui/accessibilityperformshowdefaultui.md)
  Returns to the accessibility element’s original UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui/isaccessibilityalternateuivisible())*