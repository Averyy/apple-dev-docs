# AXAnimatedImagesEnabled()

**Framework**: Accessibility  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the system setting for Animated Images is on.

**Availability**:
- iOS 17.0+ - Deprecated in 18.0 (renamed: AccessibilitySettings.animatedImagesEnabled)
- iPadOS 17.0+ - Deprecated in 18.0 (renamed: AccessibilitySettings.animatedImagesEnabled)
- Mac Catalyst 17.0+ - Deprecated in 18.0 (renamed: AccessibilitySettings.animatedImagesEnabled)
- macOS 14.0+ - Deprecated in 15.0 (renamed: AccessibilitySettings.animatedImagesEnabled)
- tvOS 17.0+ - Deprecated in 18.0 (renamed: AccessibilitySettings.animatedImagesEnabled)
- visionOS 1.0+
- watchOS 10.0+ - Deprecated in 11.0 (renamed: AccessibilitySettings.animatedImagesEnabled)

> **Deprecated**: Use [`animatedImagesEnabled`](./accessibilitysettings/animatedimagesenabled.md) instead.

## Declaration

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
func AXAnimatedImagesEnabled() -> Bool
```

## Return Value

[`true`](../Swift/true.md) if the system setting for Animated Images is on; otherwise, [`false`](../Swift/false.md).

## See Also

### Deprecated
- [func AXPrefersHeadAnchorAlternative() -> Bool](./axprefersheadanchoralternative%28%29.md)
  Returns a Boolean value that indicates the person’s preference for content that follows their head position.
- [func AXPrefersHorizontalTextLayout() -> Bool](./axprefershorizontaltextlayout%28%29.md)
  Returns a Boolean value that indicates whether the system setting for Prefer Horizontal Text is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axanimatedimagesenabled())*