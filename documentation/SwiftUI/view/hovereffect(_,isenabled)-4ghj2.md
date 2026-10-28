# hoverEffect(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies a hover effect to this view, while providing a way to conditionally enable or disable it.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func hoverEffect(_ effect: some CustomHoverEffect = .automatic, isEnabled: Bool = true) -> some View
```

**Other overloads**:

```swift
nonisolated
func hoverEffect(_ effect: HoverEffect = .automatic, isEnabled: Bool = true) -> some View
```

## Return Value

A view with the hover effect applied.

## Discussion

By default, [`automatic`](../customhovereffect/automatic.md) is used. You can control the behavior of the automatic effect with the [`defaultHoverEffect(_:)`](./defaulthovereffect%28_%29.md) modifier.

## Parameters

- `effect`: The hover effect to apply to this view.
- `isEnabled`: Whether the hover effect is enabled or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/hovereffect(_:isenabled:)-4ghj2)*