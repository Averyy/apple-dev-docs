# AXAnimatedImagesEnabled()

**Framework**: Accessibility  
**Kind**: func

Returns a Boolean value that indicates whether the system setting for Animated Images is on.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
func AXAnimatedImagesEnabled() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the system setting for Animated Images is on; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func AXPrefersHeadAnchorAlternative() -> Bool](axprefersheadanchoralternative().md)
  Returns a Boolean value that indicates the person’s preference for content that follows their head position.
- [func AXPrefersHorizontalTextLayout() -> Bool](axprefershorizontaltextlayout().md)
  Returns a Boolean value that indicates whether the system setting for Prefer Horizontal Text is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axanimatedimagesenabled())*