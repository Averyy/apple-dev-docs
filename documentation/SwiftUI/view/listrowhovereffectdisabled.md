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

- [func listRowInsets(EdgeInsets?) -> some View](view/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func listRowHoverEffect(HoverEffect?) -> some View](view/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.
- [func listItemTint(_:)](view/listitemtint(_:).md)
  Sets a fixed tint color for content in a list.
- [struct ListItemTint](listitemtint.md)
  A tint effect configuration that you can apply to content in a list.
- [var defaultMinListRowHeight: CGFloat](environmentvalues/defaultminlistrowheight.md)
  The default minimum height of a row in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listrowhovereffectdisabled(_:))*