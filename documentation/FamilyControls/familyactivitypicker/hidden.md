# hidden()

**Framework**: FamilyControls  
**Kind**: method

Hides this view unconditionally.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func hidden() -> some View
```

#### Return Value

A hidden view.

#### Discussion

Hidden views are invisible and can’t receive or respond to interactions. However, they do remain in the view hierarchy and affect layout. Use this modifier if you want to include a view for layout purposes, but don’t want it to display.

```swift
HStack {
    Image(systemName: "a.circle.fill")
    Image(systemName: "b.circle.fill")
    Image(systemName: "c.circle.fill")
        .hidden()
    Image(systemName: "d.circle.fill")
}
```

The third circle takes up space, because it’s still present, but SwiftUI doesn’t draw it onscreen.

If you want to conditionally include a view in the view hierarchy, use an `if` statement instead:

```swift
VStack {
    HStack {
        Image(systemName: "a.circle.fill")
        Image(systemName: "b.circle.fill")
        if !isHidden {
            Image(systemName: "c.circle.fill")
        }
        Image(systemName: "d.circle.fill")
    }
    Toggle("Hide", isOn: $isHidden)
}
```

Depending on the current value of the `isHidden` state variable in the example above, controlled by the `Toggle` instance, SwiftUI draws the circle or completely omits it from the layout.

## See Also

- [func labelsHidden() -> some View](familyactivitypicker/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func menuIndicator(Visibility) -> some View](familyactivitypicker/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/hidden())*