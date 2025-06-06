# widgetContentMargins

**Framework**: SwiftUI  
**Kind**: property

A property that identifies the content margins of a widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- watchOS 10.0+

## Declaration

```swift
var widgetContentMargins: EdgeInsets { get }
```

#### Return Value

Returns the content margins for the current widget presentation context.

#### Discussion

The content margins of a widget depend on the context in which it appears. The system applies default content margins. However, if you disable automatic application of default content margins with [`contentMarginsDisabled()`](WidgetConfiguration/contentMarginsDisabled().md), the system uses the `widgetContentMargins` property in combination with [`padding(_:)`](View/padding(_:).md) to selectively apply default content margins.

## See Also

- [var showsWidgetContainerBackground: Bool](environmentvalues/showswidgetcontainerbackground.md)
  An environment variable that indicates whether the background of a widget appears.
- [var showsWidgetLabel: Bool](environmentvalues/showswidgetlabel.md)
  A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [var widgetFamily: WidgetFamily](environmentvalues/widgetfamily.md)
  The template of the widget — small, medium, or large.
- [var widgetRenderingMode: WidgetRenderingMode](environmentvalues/widgetrenderingmode.md)
  The widget’s rendering mode, based on where the system is displaying it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/widgetcontentmargins)*