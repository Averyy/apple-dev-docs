# widgetLabel(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Returns a text label that displays additional content outside the accessory family widget’s main SwiftUI view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency func widgetLabel<S>(_ label: S) -> some View where S : StringProtocol
```

#### Discussion

To add a text label to an accessory family widget, call this method on the widget’s main SwiftUI view, and pass in a supported [`LocalizedStringKey`](https://developer.apple.com/documentation/SwiftUI/LocalizedStringKey). The system determines whether it can use the text label. If it can’t, it ignores the label. The system also sets the label’s size, placement, and style. For example, setting the font and rendering the text along a curve.

The following widget families support text accessory labels:

- The [`WidgetFamily.accessoryCorner`](https://developer.apple.com/documentation/WidgetKit/WidgetFamily/accessoryCorner) widget-based complication can display a curved text label on the inside edge of the corner. Adding a label to an accessory corner complication causes the main SwiftUI view to shrink to make space for the label.
- The [`WidgetFamily.accessoryCircular`](https://developer.apple.com/documentation/WidgetKit/WidgetFamily/accessoryCircular) widget can display a text label in watchOS; however, WidgetKit only renders the label along the bezel on the Infograph watch face (the top circular complication).

## Parameters

- `label`: A string that contains the text which WidgetKit   displays alongside the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/widgetlabel(_:)-88ak0)*