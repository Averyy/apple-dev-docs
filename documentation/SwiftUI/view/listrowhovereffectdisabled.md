# listRowHoverEffectDisabled(_:)

**Framework**: SwiftUI  
**Kind**: method

Requests that the containing list row have its hover effect disabled.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func listRowHoverEffectDisabled(_ disabled: Bool = true) -> some View
```

#### Return Value

A view that requests the default hover effect on its containing list row to conditionally be disabled.

#### Discussion

By default, `List` rows have built-in hover effects in visionOS. In some cases, it is useful to disable the default hover effect.

## Parameters

- `disabled`: A Boolean value that determines whether the   containing list row should display its default hover effect.

## See Also

- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some View](view/swipeactions(edge:allowsfullswipe:content:).md)
  Adds custom swipe actions to a row in a list.
- [func selectionDisabled(Bool) -> some View](view/selectiondisabled(_:).md)
  Adds a condition that controls whether users can select this view.
- [func listRowHoverEffect(HoverEffect?) -> some View](view/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listrowhovereffectdisabled(_:))*