# widgetCurvesContent(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Displays the widget’s content along a curve if the context allows it.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func widgetCurvesContent(_ curvesContent: Bool = true) -> some View
```

## Discussion

The system positions the widget’s content along a curve that follows the corner of the watch face when displaying a [`WidgetFamily.accessoryCorner`](../../WidgetKit/widgetfamily/accessorycorner.md) complication. The widget must use  a  [`widgetLabel(_:)`](./widgetlabel%28_%29-7wguh.md) modifier, and the curving effect modifies only text, SF Symbols, and images.

When displaying an `.accessoryCorner` complication, the system places the widget label on the inside of the curve, and the widget’s content on the outside, as shown below.

```swift
var body: some View {
    Text("Hi")
        .widgetCurvesContent()
        .widgetLabel("World!")
}
```

The system can also curve text, SF symbols, and image content from a [`ViewThatFits`](../viewthatfits.md) view.

```swift
var body: some View {
    ViewThatFits {
        Text("Hello")
        Text("Hi")
    }
    .widgetCurvesContent()
    .widgetLabel("World!")
}
```

## Parameters

- `curvesContent`: A Boolean value that indicates whether the system curves the widget label’s content, if the context allows.

## See Also

### Widget configuration
- [func widgetAccentable(Bool) -> some View](./widgetaccentable%28_%29.md)
  Adds the view and all of its subviews to the accented group.
- [func widgetLabel(_:)](./widgetlabel%28_%29.md)
  Returns a localized text label that displays additional content outside the accessory family widget’s main SwiftUI view.
- [func widgetLabel<Label>(label: () -> Label) -> some View](./widgetlabel%28label%29.md)
  Creates a label for displaying additional content outside an accessory family widget’s main SwiftUI view.
- [func dynamicIsland(verticalPlacement: DynamicIslandExpandedRegionVerticalPlacement) -> some View](./dynamicisland%28verticalplacement%29.md)
  Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [func accessoryWidgetGroupStyle(AccessoryWidgetGroupStyle) -> some View](./accessorywidgetgroupstyle%28_%29.md)
  The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three content views will be masked with. The value of `style` is set to `.automatic`, which is `.circular` by default.
- [func controlWidgetActionHint(_:)](./controlwidgetactionhint%28_%29.md)
  The action hint of the control described by the modified label.
- [func controlWidgetStatus(_:)](./controlwidgetstatus%28_%29.md)
  The status of the control described by the modified label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/widgetcurvescontent(_:))*