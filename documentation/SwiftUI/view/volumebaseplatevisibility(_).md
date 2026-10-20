# volumeBaseplateVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

### Visibility
- [func hidden() -> some View](./hidden%28%29.md)
  Hides this view unconditionally.
- [func labelsHidden() -> some View](./labelshidden%28%29.md)
  Hides the labels of any controls contained within this view.
- [func labelsVisibility(Visibility) -> some View](./labelsvisibility%28_%29.md)
  Controls the visibility of labels of any controls contained within this view.
- [func menuIndicator(Visibility) -> some View](./menuindicator%28_%29.md)
  Sets the menu indicator visibility for controls within this view.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](./listrowseparator%28_,edges%29.md)
  Sets the display mode for the separator associated with this specific row.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](./listsectionseparator%28_,edges%29.md)
  Sets whether to hide the separator associated with a list section.
- [func listSectionIndexVisibility(Visibility) -> some View](./listsectionindexvisibility%28_%29.md)
  Changes the visibility of the list section index.
- [func persistentSystemOverlays(Visibility) -> some View](./persistentsystemoverlays%28_%29.md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](./scrollindicators%28_,axes%29.md)
  Sets the visibility of scroll indicators within this view.
- [func scrollClipDisabled(Bool) -> some View](./scrollclipdisabled%28_%29.md)
  Sets whether a scroll view clips its content to its bounds.
- [func sliderThumbVisibility(Visibility) -> some View](./sliderthumbvisibility%28_%29.md)
  Sets the thumb visibility for `Slider`s within this view.
- [func tableColumnHeaders(Visibility) -> some View](./tablecolumnheaders%28_%29.md)
  Controls the visibility of a `Table`’s column header views.
- [func upperLimbVisibility(Visibility) -> some View](./upperlimbvisibility%28_%29.md)
  Sets the preferred visibility of the user’s upper limbs, while an [`ImmersiveSpace`](../immersivespace.md) scene is presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/volumebaseplatevisibility(_:))*