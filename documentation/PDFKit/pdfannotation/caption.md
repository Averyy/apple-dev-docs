# caption

**Framework**: PDFKit  
**Kind**: property

The title of push button widget annotations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var caption: String? { get set }
```

## See Also

- [var widgetControlType: PDFWidgetControlType](pdfannotation/widgetcontroltype.md)
  The type of button widget control, either radio button, push button, or checkbox.
- [var buttonWidgetState: PDFWidgetCellState](pdfannotation/buttonwidgetstate.md)
  The current state of the button widget annotation.
- [enum PDFWidgetCellState](pdfwidgetcellstate.md)
  The state of a button annotation, either on, off, or mixed.
- [var buttonWidgetStateString: String](pdfannotation/buttonwidgetstatestring.md)
  A string value that differentiates button widgets in the same group, such as to identify mutually exclusive radio buttons from each other.
- [var allowsToggleToOff: Bool](pdfannotation/allowstoggletooff.md)
  A Boolean value that indicates whether clicking or tapping a selected radio button toggles it to an unselected state.
- [var radiosInUnison: Bool](pdfannotation/radiosinunison.md)
  A Boolean value that indicates whether radio buttons in a group turn on and off in unison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/caption)*