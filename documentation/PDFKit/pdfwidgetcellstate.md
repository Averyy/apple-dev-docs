# PDFWidgetCellState

**Framework**: PDFKit  
**Kind**: enum

The state of a button annotation, either on, off, or mixed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum PDFWidgetCellState
```

## Topics

### Choosing a Cell State
- [PDFWidgetCellState.onState](pdfwidgetcellstate/onstate.md)
  The button widget is in a selected state.
- [PDFWidgetCellState.offState](pdfwidgetcellstate/offstate.md)
  The button widget is in an unselected state.
- [PDFWidgetCellState.mixedState](pdfwidgetcellstate/mixedstate.md)
  The button widget is in a mixed state, neither on nor off.
### Initializers
- [init?(rawValue: Int)](pdfwidgetcellstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var widgetControlType: PDFWidgetControlType](pdfannotation/widgetcontroltype.md)
  The type of button widget control, either radio button, push button, or checkbox.
- [var buttonWidgetState: PDFWidgetCellState](pdfannotation/buttonwidgetstate.md)
  The current state of the button widget annotation.
- [var buttonWidgetStateString: String](pdfannotation/buttonwidgetstatestring.md)
  A string value that differentiates button widgets in the same group, such as to identify mutually exclusive radio buttons from each other.
- [var caption: String?](pdfannotation/caption.md)
  The title of push button widget annotations.
- [var allowsToggleToOff: Bool](pdfannotation/allowstoggletooff.md)
  A Boolean value that indicates whether clicking or tapping a selected radio button toggles it to an unselected state.
- [var radiosInUnison: Bool](pdfannotation/radiosinunison.md)
  A Boolean value that indicates whether radio buttons in a group turn on and off in unison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfwidgetcellstate)*