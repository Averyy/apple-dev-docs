# volumeBaseplateVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func volumeBaseplateVisibility(_ visibility: Visibility) -> some View
```

#### Discussion

The baseplate is a semi-transparent view that appears on the ‘floor’ of a volume.

Usage:

```swift
WindowGroup() {
    Poker()
        .volumeBaseplateVisibility(.visible)
}
.windowStyle(.volumetric)
```

Defaults to `automatic` (visible).

## See Also

- [func hidden() -> some View](view/hidden.md)
  Hides this view unconditionally.
- [func labelsHidden() -> some View](view/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func menuIndicator(Visibility) -> some View](view/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.
- [func persistentSystemOverlays(Visibility) -> some View](view/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](view/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [func scrollClipDisabled(Bool) -> some View](view/scrollclipdisabled(_:).md)
  Sets whether a scroll view clips its content to its bounds.
- [func tableColumnHeaders(Visibility) -> some View](view/tablecolumnheaders(_:).md)
  Controls the visibility of a `Table`’s column header views.
- [func upperLimbVisibility(Visibility) -> some View](view/upperlimbvisibility(_:).md)
  Sets the preferred visibility of the user’s upper limbs, while an [`ImmersiveSpace`](immersivespace.md) scene is presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/volumebaseplatevisibility(_:))*