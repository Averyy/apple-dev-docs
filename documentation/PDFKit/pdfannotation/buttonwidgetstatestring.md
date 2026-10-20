# buttonWidgetStateString

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

A string value that differentiates button widgets in the same group, such as to identify mutually exclusive radio buttons from each other.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var buttonWidgetStateString: String { get set }
```

```objc
@property (nonatomic, copy) NSString * buttonWidgetStateString;
```

## Mentions

- [Adding Widgets to a PDF Document](../adding-widgets-to-a-pdf-document.md)

#### Discussion

The default value is `Yes`.

To group button widgets, set the same [`fieldName`](./fieldname.md) on the button widgets. The [`buttonWidgetStateString`](./buttonwidgetstatestring.md) property allows you to identify individual button widgets in that group.

## See Also

### Configuring Button Widget Annotations
- [var widgetControlType: PDFWidgetControlType](./widgetcontroltype.md)
  The type of button widget control, either radio button, push button, or checkbox.
- [var buttonWidgetState: PDFWidgetCellState](./buttonwidgetstate.md)
  The current state of the button widget annotation.
- [enum PDFWidgetCellState](../pdfwidgetcellstate.md)
  The state of a button annotation, either on, off, or mixed.
- [var caption: String?](./caption.md)
  The title of push button widget annotations.
- [var allowsToggleToOff: Bool](./allowstoggletooff.md)
  A Boolean value that indicates whether clicking or tapping a selected radio button toggles it to an unselected state.
- [var radiosInUnison: Bool](./radiosinunison.md)
  A Boolean value that indicates whether radio buttons in a group turn on and off in unison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/buttonwidgetstatestring)*