# AXPrefersHorizontalTextLayout()

**Framework**: Accessibility  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the system setting for Prefer Horizontal Text is on.

**Availability**:
- iOS 17.0+ - Deprecated in 18.0 (renamed: AccessibilitySettings.prefersHorizontalTextLayout)
- iPadOS 17.0+ - Deprecated in 18.0 (renamed: AccessibilitySettings.prefersHorizontalTextLayout)
- Mac Catalyst 17.0+ - Deprecated in 18.0 (renamed: AccessibilitySettings.prefersHorizontalTextLayout)
- macOS 14.0+ - Deprecated in 15.0 (renamed: AccessibilitySettings.prefersHorizontalTextLayout)
- tvOS 17.0+ - Deprecated in 18.0 (renamed: AccessibilitySettings.prefersHorizontalTextLayout)
- visionOS 1.0+
- watchOS 10.0+ - Deprecated in 11.0 (renamed: AccessibilitySettings.prefersHorizontalTextLayout)

> **Deprecated**: Use [`prefersHorizontalTextLayout`](./accessibilitysettings/prefershorizontaltextlayout.md) instead.

## Declaration

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
func AXPrefersHorizontalTextLayout() -> Bool
```

## Return Value

[`true`](../Swift/true.md) if the system setting for Prefer Horizontal Text is on; otherwise, [`false`](../Swift/false.md).

## See Also

### Deprecated
- [func AXAnimatedImagesEnabled() -> Bool](./axanimatedimagesenabled%28%29.md)
  Returns a Boolean value that indicates whether the system setting for Animated Images is on.
- [func AXPrefersHeadAnchorAlternative() -> Bool](./axprefersheadanchoralternative%28%29.md)
  Returns a Boolean value that indicates the person’s preference for content that follows their head position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axprefershorizontaltextlayout())*