# buttonWidgetStateString

**Framework**: PDFKit  
**Kind**: property

A string value that differentiates button widgets in the same group, such as to identify mutually exclusive radio buttons from each other.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var buttonWidgetStateString: String { get set }
```

## Mentions

- [Adding Widgets to a PDF Document](adding-widgets-to-a-pdf-document.md)

#### Discussion

The default value is `Yes`.

To group button widgets, set the same [`fieldName`](pdfannotation/fieldname.md) on the button widgets. The [`buttonWidgetStateString`](pdfannotation/buttonwidgetstatestring.md) property allows you to identify individual button widgets in that group.

## See Also

- [var widgetControlType: PDFWidgetControlType](pdfannotation/widgetcontroltype.md)
  The type of button widget control, either radio button, push button, or checkbox.
- [var buttonWidgetState: PDFWidgetCellState](pdfannotation/buttonwidgetstate.md)
  The current state of the button widget annotation.
- [enum PDFWidgetCellState](pdfwidgetcellstate.md)
  The state of a button annotation, either on, off, or mixed.
- [var caption: String?](pdfannotation/caption.md)
  The title of push button widget annotations.
- [var allowsToggleToOff: Bool](pdfannotation/allowstoggletooff.md)
  A Boolean value that indicates whether clicking or tapping a selected radio button toggles it to an unselected state.
- [var radiosInUnison: Bool](pdfannotation/radiosinunison.md)
  A Boolean value that indicates whether radio buttons in a group turn on and off in unison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/buttonwidgetstatestring)*