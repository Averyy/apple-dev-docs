# widgetRenderingMode

**Framework**: SwiftUI  
**Kind**: property

The widget’s rendering mode, based on where the system is displaying it.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
var widgetRenderingMode: WidgetRenderingMode { get set }
```

#### Discussion

You can read the rendering mode from the environment values using this key.

```swift
@Environment(\.widgetRenderingMode) var widgetRenderingMode
```

Then modify the widget’s appearance based on the mode.

```swift
var body: some View {
    ZStack {
       switch renderingMode {
        case .fullColor:
           Text("Full color")
        case .accented:
           ZStack {
               Circle(...)
               VStack {
                   Text("Accented")
                       .widgetAccentable()
                   Text("Normal")
               }
           }
        case .vibrant:
           Text("Full color")
        default:
           ...
        }
    }
}
```

## See Also

- [var showsWidgetContainerBackground: Bool](environmentvalues/showswidgetcontainerbackground.md)
  An environment variable that indicates whether the background of a widget appears.
- [var showsWidgetLabel: Bool](environmentvalues/showswidgetlabel.md)
  A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [var widgetFamily: WidgetFamily](environmentvalues/widgetfamily.md)
  The template of the widget — small, medium, or large.
- [var widgetContentMargins: EdgeInsets](environmentvalues/widgetcontentmargins.md)
  A property that identifies the content margins of a widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/widgetrenderingmode)*