# showsWidgetContainerBackground

**Framework**: SwiftUI  
**Kind**: property

An environment variable that indicates whether the background of a widget appears.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- watchOS 8.0+

## Declaration

```swift
var showsWidgetContainerBackground: Bool { get }
```

#### Return Value

`true` if, by default, the background appears in this context; `false` otherwise.

#### Discussion

In iOS 16 and earlier, this environment variable is always `true` for system widgets and `false` for accessory widgets. In macOS 13 and earlier, and in watchOS 9 and earlier, it always evaluates to `true`.

If you pass `false` to [`containerBackgroundRemovable(_:)`](WidgetConfiguration/containerBackgroundRemovable(_:).md) to always show the widget background, the system shows the widget background even if `showsWidgetContainerBackground` evaluates to `true`.

## See Also

- [var showsWidgetLabel: Bool](environmentvalues/showswidgetlabel.md)
  A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [var widgetFamily: WidgetFamily](environmentvalues/widgetfamily.md)
  The template of the widget — small, medium, or large.
- [var widgetRenderingMode: WidgetRenderingMode](environmentvalues/widgetrenderingmode.md)
  The widget’s rendering mode, based on where the system is displaying it.
- [var widgetContentMargins: EdgeInsets](environmentvalues/widgetcontentmargins.md)
  A property that identifies the content margins of a widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/showswidgetcontainerbackground)*