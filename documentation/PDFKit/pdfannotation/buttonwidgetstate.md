# buttonWidgetState

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The current state of the button widget annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var buttonWidgetState: PDFWidgetCellState { get set }
```

```objc
@property (nonatomic) PDFWidgetCellState buttonWidgetState;
```

## See Also

### Configuring Button Widget Annotations
- [var widgetControlType: PDFWidgetControlType](./widgetcontroltype.md)
  The type of button widget control, either radio button, push button, or checkbox.
- [enum PDFWidgetCellState](../pdfwidgetcellstate.md)
  The state of a button annotation, either on, off, or mixed.
- [var buttonWidgetStateString: String](./buttonwidgetstatestring.md)
  A string value that differentiates button widgets in the same group, such as to identify mutually exclusive radio buttons from each other.
- [var caption: String?](./caption.md)
  The title of push button widget annotations.
- [var allowsToggleToOff: Bool](./allowstoggletooff.md)
  A Boolean value that indicates whether clicking or tapping a selected radio button toggles it to an unselected state.
- [var radiosInUnison: Bool](./radiosinunison.md)
  A Boolean value that indicates whether radio buttons in a group turn on and off in unison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/buttonwidgetstate)*