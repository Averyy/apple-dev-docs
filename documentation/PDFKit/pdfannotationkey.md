# PDFAnnotationKey

**Framework**: PDFKit  
**Kind**: struct

Keys for setting properties of annotations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct PDFAnnotationKey
```

## Topics

### Configuring General Properties
- [static let contents: PDFAnnotationKey](pdfannotationkey/contents.md)
  The text that the annotation displays or represents.
- [static let date: PDFAnnotationKey](pdfannotationkey/date.md)
  The date, or string representation of a date, of the annotation’s most recent modification.
- [static let flags: PDFAnnotationKey](pdfannotationkey/flags.md)
  An integer value that specifies flags for the annotation.
- [static let name: PDFAnnotationKey](pdfannotationkey/name.md)
  A string that uniquely identifies the annotation among all annotations on the same page.
- [static let page: PDFAnnotationKey](pdfannotationkey/page.md)
  A dictionary or PDF page object that includes the annotation.
- [static let parent: PDFAnnotationKey](pdfannotationkey/parent.md)
  A dictionary or annotation object that a pop-up or widget belongs to.
- [static let quadPoints: PDFAnnotationKey](pdfannotationkey/quadpoints.md)
  An array of floating point values that specifies a rectangular region of a page.
- [static let rect: PDFAnnotationKey](pdfannotationkey/rect.md)
  The rectangle that the annotation occupies on the page, in page-space coordinates.
- [static let subtype: PDFAnnotationKey](pdfannotationkey/subtype.md)
  The type of annotation that the entries in a dictionary describe.
- [static let textLabel: PDFAnnotationKey](pdfannotationkey/textlabel.md)
  A string that represents the title of the annotation.
### Configuring Annotation Appearance
- [static let appearanceDictionary: PDFAnnotationKey](pdfannotationkey/appearancedictionary.md)
  A dictionary that contains properties for controlling the annotation’s visual appearance.
- [static let appearanceState: PDFAnnotationKey](pdfannotationkey/appearancestate.md)
  A string that specifies the appearance stream for the annotation.
- [static let border: PDFAnnotationKey](pdfannotationkey/border.md)
  An array of integers or border objects that describes the border of the annotation.
- [static let borderStyle: PDFAnnotationKey](pdfannotationkey/borderstyle.md)
  A dictionary that contains the properties of the annotation’s border.
- [static let color: PDFAnnotationKey](pdfannotationkey/color.md)
  An array of floats or a color object that specifies the annotation’s color.
- [static let defaultAppearance: PDFAnnotationKey](pdfannotationkey/defaultappearance.md)
  A string value a free text annotation uses to format the text.
- [static let highlightingMode: PDFAnnotationKey](pdfannotationkey/highlightingmode.md)
  A string value that defines the way an annotation highlights when the user activates it, such as when clicking or tapping a link.
- [struct PDFAnnotationHighlightingMode](pdfannotationhighlightingmode.md)
- [static let iconName: PDFAnnotationKey](pdfannotationkey/iconname.md)
  A string value that specifies the name of an icon for a text or stamp annotation.
- [static let interiorColor: PDFAnnotationKey](pdfannotationkey/interiorcolor.md)
  An array of floating point values or a PDF color object that annotations use to fill interior space, such as line endings, squares, or circles.
- [static let quadding: PDFAnnotationKey](pdfannotationkey/quadding.md)
  An integer value that specifies left, right, or center justification.
### Configuring Line Properties
- [static let lineEndingStyles: PDFAnnotationKey](pdfannotationkey/lineendingstyles.md)
  An array of string values that specifies the styles to use for the ends of lines.
- [enum PDFLineStyle](pdflinestyle.md)
  The following constants specify the available line ending styles.
- [static let linePoints: PDFAnnotationKey](pdfannotationkey/linepoints.md)
  An array of floating point values that specifies the starting and ending points, in page-space coordinates, of a line.
- [struct PDFAnnotationLineEndingStyle](pdfannotationlineendingstyle.md)
### Configuring Pop-Up Annotations
- [static let popup: PDFAnnotationKey](pdfannotationkey/popup.md)
  A dictionary or annotation object that specifies the annotation to pop up for text entry or editing.
- [static let open: PDFAnnotationKey](pdfannotationkey/open.md)
  A Boolean value that specifies whether the pop-up is in an opened state, showing its text content, or in a closed state and showing an icon.
### Configuring Widget Annotations
- [static let widgetAppearanceDictionary: PDFAnnotationKey](pdfannotationkey/widgetappearancedictionary.md)
  A dictionary or appearance characteristic object that contains properties for controlling the widget’s visual appearance.
- [static let widgetBackgroundColor: PDFAnnotationKey](pdfannotationkey/widgetbackgroundcolor.md)
  An array of floating point values or a PDF color object that specifies the widget’s background color.
- [static let widgetBorderColor: PDFAnnotationKey](pdfannotationkey/widgetbordercolor.md)
  An array of floating point values or a PDF color object that specifies the widget’s border color.
- [static let widgetCaption: PDFAnnotationKey](pdfannotationkey/widgetcaption.md)
  A string that a push button widget displays when it isn’t in a pressed state.
- [static let widgetDefaultValue: PDFAnnotationKey](pdfannotationkey/widgetdefaultvalue.md)
  A default value for the widget.
- [static let widgetDownCaption: PDFAnnotationKey](pdfannotationkey/widgetdowncaption.md)
  A string that a push button widgets displays when it’s in a pressed state.
- [static let widgetFieldFlags: PDFAnnotationKey](pdfannotationkey/widgetfieldflags.md)
  An integer value that specifies flags for a widget.
- [static let widgetFieldType: PDFAnnotationKey](pdfannotationkey/widgetfieldtype.md)
  A string that specifies the type of widget, such as button, checkbox, or signature field.
- [static let widgetMaxLen: PDFAnnotationKey](pdfannotationkey/widgetmaxlen.md)
  An integer value that specifies the maximum length of a text field, in characters.
- [static let widgetOptions: PDFAnnotationKey](pdfannotationkey/widgetoptions.md)
  An array that specifies the options to present in radio buttons or choice lists.
- [static let widgetRolloverCaption: PDFAnnotationKey](pdfannotationkey/widgetrollovercaption.md)
  A string that push button widgets display when the pointer is over the button, but not clicking it.
- [static let widgetRotation: PDFAnnotationKey](pdfannotationkey/widgetrotation.md)
  An integer value that specifies the rotation of the widget.
- [static let widgetTextLabelUI: PDFAnnotationKey](pdfannotationkey/widgettextlabelui.md)
  A user-visible alternative field name that identifies the widget, typically for accessibility purposes.
- [static let widgetValue: PDFAnnotationKey](pdfannotationkey/widgetvalue.md)
  The widget’s value, typically for text and choice widgets.
- [struct PDFAnnotationWidgetSubtype](pdfannotationwidgetsubtype.md)
### Configuring Actions
- [static let destination: PDFAnnotationKey](pdfannotationkey/destination.md)
  An array, name, or string that represents the destination of an action.
- [static let action: PDFAnnotationKey](pdfannotationkey/action.md)
  A dictionary or PDF action object that represents an action to take, such as when the user clicks or taps a button.
- [static let additionalActions: PDFAnnotationKey](pdfannotationkey/additionalactions.md)
  A dictionary or PDF action object that represents additional actions an annotation can perform, such as when it receives input focus.
### Configuring Ink Annotations
- [static let inklist: PDFAnnotationKey](pdfannotationkey/inklist.md)
  An array of arrays that represents stroked paths.
### Creating an Annotation Key
- [init(rawValue: String)](pdfannotationkey/init(rawvalue:).md)
  Creates an annotation key using the specified raw string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var annotationKeyValues: [AnyHashable : Any]](pdfannotation/annotationkeyvalues.md)
  A dictionary that contains a deep copy of the widget’s properties.
- [func value(forAnnotationKey: PDFAnnotationKey) -> Any?](pdfannotation/value(forannotationkey:).md)
  Returns a deep copy of the key-value pairs of properties for the specified key.
- [func setValue(Any, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setvalue(_:forannotationkey:).md)
  Sets a value in the annotation’s dictionary.
- [func setBoolean(Bool, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setboolean(_:forannotationkey:).md)
  Sets a Boolean value in the annotation’s dictionary.
- [func setRect(CGRect, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setrect(_:forannotationkey:).md)
  Sets a rectangle value in the annotation’s dictionary.
- [func removeValue(forAnnotationKey: PDFAnnotationKey)](pdfannotation/removevalue(forannotationkey:).md)
  Removes a value from the annotation’s dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotationkey)*