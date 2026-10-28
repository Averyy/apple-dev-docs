# listRowHoverEffect(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Requests that the containing list row use the provided hover effect.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func listRowHoverEffect(_ effect: HoverEffect?) -> some View
```

## Return Value

A view that requests a hover effect for a containing list row

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some cases, it is useful to change the default hover effect.

This modifier can be applied to a list row’s content to request that the list row’s default effect be replaced by the provided effect. If the view is not contained within a `List` or if the view does not support hover effects in this context, the modifier has no effect.

Use a `nil` effect to indicate that the list row’s default hover effect should not be modified.

[`lift`](../hovereffect/lift.md) is not supported for list rows.

## Parameters

- `effect`: The hover effect applied to the entire list row.

## See Also

### Configuring interaction
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](./swipeactions%28edge,allowsfullswipe,content%29.md)
  Adds custom swipe actions to a row in a list.
- [func selectionDisabled(Bool) -> some View](./selectiondisabled%28_%29.md)
  Adds a condition that controls whether users can select this view.
- [func listRowHoverEffectDisabled(Bool) -> some View](./listrowhovereffectdisabled%28_%29.md)
  Requests that the containing list row have its hover effect disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listrowhovereffect(_:))*