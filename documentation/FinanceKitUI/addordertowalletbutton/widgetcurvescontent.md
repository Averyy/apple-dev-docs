# widgetCurvesContent(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Displays the widget’s content along a curve if the context allows it.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func widgetCurvesContent(_ curvesContent: Bool = true) -> some View
```

#### Discussion

The system positions the widget’s content along a curve that follows the corner of the watch face when displaying a [`WidgetFamily.accessoryCorner`](https://developer.apple.com/documentation/WidgetKit/WidgetFamily/accessoryCorner) complication. The widget must use  a  [`widgetLabel(_:)`](https://developer.apple.com/documentation/SwiftUI/View/widgetLabel(_:)-7wguh) modifier, and the curving effect modifies only text, SF Symbols, and images.

When displaying an `.accessoryCorner` complication, the system places the widget label on the inside of the curve, and the widget’s content on the outside, as shown below.

```swift
var body: some View {
    Text("Hi")
        .widgetCurvesContent()
        .widgetLabel("World!")
}
```

The system can also curve text, SF symbols, and image content from a [`ViewThatFits`](https://developer.apple.com/documentation/SwiftUI/ViewThatFits) view.

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

- `curvesContent`: A Boolean value that indicates whether the   system curves the widget label’s content, if the context allows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/widgetcurvescontent(_:))*