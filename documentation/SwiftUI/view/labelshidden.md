# labelsHidden()

**Framework**: SwiftUI  
**Kind**: method

Hides the labels of any controls contained within this view.

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
func labelsHidden() -> some View
```

#### Discussion

Use this modifier when you want to omit a label from one or more controls in your user interface. For example, the first [`Toggle`](toggle.md) in the following example hides its label:

```swift
VStack {
    Toggle(isOn: $toggle1) {
        Text("Toggle 1")
    }
    .labelsHidden()

    Toggle(isOn: $toggle2) {
        Text("Toggle 2")
    }
}
```

The [`VStack`](vstack.md) in the example above centers the first toggle’s control element in the available space, while it centers the second toggle’s combined label and control element:

![A screenshot showing a view with two toggle controls where one label](https://docs-assets.developer.apple.com/published/2f1d6257593725bab61b7e3d52b8e2d0/View-labelsHidden-1%402x.png)

Always provide a label for controls, even when you hide the label, because SwiftUI uses labels for other purposes, including accessibility.

> **Note**: This modifier doesn’t work for all labels. It applies to labels that are separate from the rest of the control’s interface, like they are for [`Toggle`](toggle.md), but not to controls like a bordered button where the label is inside the button’s border.

This modifier doesn’t work for all labels. It applies to labels that are separate from the rest of the control’s interface, like they are for [`Toggle`](toggle.md), but not to controls like a bordered button where the label is inside the button’s border.

## See Also

- [func labelsVisibility(Visibility) -> some View](view/labelsvisibility(_:).md)
  Controls the visibility of labels of any controls contained within this view.
- [var labelsVisibility: Visibility](environmentvalues/labelsvisibility.md)
  The labels visibility set by [`labelsVisibility(_:)`](view/labelsvisibility(_:).md).
- [func menuIndicator(Visibility) -> some View](view/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [func statusBarHidden(Bool) -> some View](view/statusbarhidden(_:).md)
  Sets the visibility of the status bar.
- [func persistentSystemOverlays(Visibility) -> some View](view/persistentsystemoverlays(_:).md)
  Sets the preferred visibility of the non-transient system views overlaying the app.
- [enum Visibility](visibility.md)
  The visibility of a UI element, chosen automatically based on the platform, current context, and other factors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/labelshidden())*