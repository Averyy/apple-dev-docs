# animation(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies the given animation to all animatable values within this view.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.0+ - Deprecated in 15.0
- macOS 10.15+ - Deprecated in 12.0
- tvOS 13.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: Use [`withAnimation(_:_:)`](../withanimation%28_,_%29.md) or [`animation(_:value:)`](./animation%28_,value%29.md) instead.

## Declaration

```swift
nonisolated
func animation(_ animation: Animation?) -> some View
```

**Other overloads**:

```swift
nonisolated
func animation(_ animation: Animation?) -> some View
```

## Return Value

A view that wraps this view and applies `animation` to all animatable values used within the view.

## Discussion

Use this modifier on leaf views rather than container views. The animation applies to all child views within this view; calling `animation(_:)` on a container view can lead to unbounded scope.

## Parameters

- `animation`: The animation to apply to animatable values within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/animation(_:)-1hc0p)*