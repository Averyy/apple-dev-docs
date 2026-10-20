# AXPrefersHeadAnchorAlternative()

**Framework**: Accessibility  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates the person’s preference for content that follows their head position.

**Availability**:
- visionOS 1.0+ - Deprecated in 2.0 (renamed: AccessibilitySettings.prefersHeadAnchorAlternative)

> **Deprecated**: Use [`prefersHeadAnchorAlternative`](./accessibilitysettings/prefersheadanchoralternative.md) instead.

## Declaration

```swift
@backDeployed(before: visionOS 2.0)
func AXPrefersHeadAnchorAlternative() -> Bool
```

#### Return Value

`true` if the person doesn’t want content anchored to their head position, or `false` if anchoring content to the head position is acceptable.

#### Discussion

On Apple Vision Pro, apps can create a heads-up display effect by setting up content to follow the person’s head position. This effect allows the content to remain in the same position, no matter where the person looks. However, some assistive technologies are incompatible with this type of content. For example, a technology might use the person’s head movements to control the current selection. Anchoring content to the head position prevents affected technologies from interacting with that content.

If your app contains head-anchored content, call this function before you display that content. If the function returns `true`, find alternate ways to display your content. For example, display it in a regular window.

## See Also

### Deprecated
- [func AXAnimatedImagesEnabled() -> Bool](./axanimatedimagesenabled%28%29.md)
  Returns a Boolean value that indicates whether the system setting for Animated Images is on.
- [func AXPrefersHorizontalTextLayout() -> Bool](./axprefershorizontaltextlayout%28%29.md)
  Returns a Boolean value that indicates whether the system setting for Prefer Horizontal Text is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axprefersheadanchoralternative())*