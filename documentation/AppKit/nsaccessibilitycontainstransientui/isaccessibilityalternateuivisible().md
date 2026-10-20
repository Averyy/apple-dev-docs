# isAccessibilityAlternateUIVisible()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that determines whether the accessibility element’s alternative UI is currently visible.

**Availability**:
- macOS

## Declaration

```swift
func isAccessibilityAlternateUIVisible() -> Bool
```

```objc
- (BOOL) isAccessibilityAlternateUIVisible;
```

#### Return Value

Use this property for elements that present an alternate UI—for example, when the pointer hovers over an interface element for a few seconds.

## See Also

### Supporting Accessibility
- [func accessibilityPerformShowAlternateUI() -> Bool](./accessibilityperformshowalternateui%28%29.md)
  Displays the accessibility element’s alternative UI.
- [func accessibilityPerformShowDefaultUI() -> Bool](./accessibilityperformshowdefaultui%28%29.md)
  Returns to the accessibility element’s original UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycontainstransientui/isaccessibilityalternateuivisible())*