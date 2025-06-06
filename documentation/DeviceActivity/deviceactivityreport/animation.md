# animation(_:)

**Framework**: DeviceActivity  
**Kind**: method

Applies the given animation to all animatable values within this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func animation(_ animation: Animation?) -> some View
```

#### Return Value

A view that wraps this view and applies `animation` to all animatable values used within the view.

#### Discussion

Use this modifier on leaf views rather than container views. The animation applies to all child views within this view; calling `animation(_:)` on a container view can lead to unbounded scope.

## Parameters

- `animation`: The animation to apply to animatable values   within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/animation(_:))*