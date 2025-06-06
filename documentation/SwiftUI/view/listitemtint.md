# listItemTint(_:)

**Framework**: Swiftui  
**Kind**: method

Sets a fixed tint color for content in a list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func listItemTint(_ tint: Color?) -> some View
```

#### Discussion

The containing list’s style applies the tint as appropriate. For example, watchOS uses the tint color for its background platter appearance. Sidebars on iOS and macOS apply the tint color to their [`Label`](label.md) icons, which otherwise use the accent color by default.

> **Note**: This modifier is equivalent to using the version of the modifier that takes a [`ListItemTint`](listitemtint.md) value and specifying the `tint` color in the corresponding [`fixed(_:)`](listitemtint/fixed(_:).md) input.

## Parameters

- `tint`: The color to use to tint the content. Use   to   avoid overriding the inherited tint.

## See Also

- [func listRowInsets(EdgeInsets?) -> some View](view/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [func listRowHoverEffect(HoverEffect?) -> some View](view/listrowhovereffect(_:).md)
  Requests that the containing list row use the provided hover effect.
- [func listRowHoverEffectDisabled(Bool) -> some View](view/listrowhovereffectdisabled(_:).md)
  Requests that the containing list row have its hover effect disabled.
- [struct ListItemTint](listitemtint.md)
  A tint effect configuration that you can apply to content in a list.
- [var defaultMinListRowHeight: CGFloat](environmentvalues/defaultminlistrowheight.md)
  The default minimum height of a row in a `List`. The default minimum height of a row in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listitemtint(_:))*