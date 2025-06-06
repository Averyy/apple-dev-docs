# Adding Widgets to a PDF Document

**Framework**: PDFKit

Add text, button, and choice widgets to a PDF document.

#### Overview

Widgets are interactive form elements that you can add to a PDF to make it easier to enter and submit information. Widgets are a special annotation subtype. To learn more about non-interactive custom annotations, see [`Adding Custom Graphics to a PDF`](adding-custom-graphics-to-a-pdf.md).

Each widget type has several variations. A button can be a radio button, a check box, or a push button. A choice widget can be a list box, which is a table of options, or a combo box, which is like a dropdown.

![Add widgets to create a form in a PDF.](https://docs-assets.developer.apple.com/published/5e2cf8f257a11f3a8193f4c25133a9ee/media-3039567%402x.png)

##### Create a Widget Annotation

Create a PDF annotation of type [`widget`](pdfannotationsubtype/widget.md). This example initializes a widget annotation with rectangular bounds:

```swift
let radioButton = PDFAnnotation(bounds: CGRect(x: 135, y: 200, width: 24, height: 24), forType: .widget, withProperties: nil)
```

##### Specify a Field Type and a Control Type

Specify a [`widgetFieldType`](pdfannotation/widgetfieldtype.md) that is a [`PDFAnnotationWidgetSubtype`](pdfannotationwidgetsubtype.md). The three different subtypes are [`text`](pdfannotationwidgetsubtype/text.md), [`button`](pdfannotationwidgetsubtype/button.md), and [`choice`](pdfannotationwidgetsubtype/choice.md). Here you will create a button widget for the radio button:

```swift
radioButton.widgetFieldType = .button

```

Set the widget control type. For a button widget, there are three possible control types: [`PDFWidgetControlType.radioButtonControl`](pdfwidgetcontroltype/radiobuttoncontrol.md), [`PDFWidgetControlType.checkBoxControl`](pdfwidgetcontroltype/checkboxcontrol.md), and [`PDFWidgetControlType.pushButtonControl`](pdfwidgetcontroltype/pushbuttoncontrol.md).

```swift
radioButton.widgetControlType = .radioButtonControl

```

##### Adjust Widget Properties

Adjust properties to highlight the widget so it is more visible. The following example adds a blue background to a radio button widget.

```swift
radioButton.backgroundColor = UIColor.blue

```

Properties will be different depending on the field type. If you have multiple radio buttons and want to group them together, specify the same [`fieldName`](pdfannotation/fieldname.md) property. Specify different [`buttonWidgetStateString`](pdfannotation/buttonwidgetstatestring.md) properties for each button if you should only select one at a time. For a text field, you can use [`widgetStringValue`](pdfannotation/widgetstringvalue.md) to specify placeholder text and [`font`](pdfannotation/font.md) to specify the font of the field’s text.

##### Add the Annotation to Your Pdf

Add the annotation to the page.

```swift
page.addAnnotation(radioButton)

```

You can combine many different kinds of widgets on your PDF. Using a combination of widgets can help you turn a PDF document into an interactive form. For more details on widget options, see [`PDFAnnotation`](pdfannotation.md).

## See Also

- [Adding Custom Graphics to a PDF](adding-custom-graphics-to-a-pdf.md)
  Create and add custom annotation and page graphics to your PDF document.
- [Custom Graphics](custom-graphics.md)
  Demonstrates adding a watermark to a PDF page.
- [PDF Widgets](pdf-widgets.md)
  Demonstrates adding widgets—interactive form elements—to a PDF document.
- [class PDFAnnotation](pdfannotation.md)
  An annotation in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/adding-widgets-to-a-pdf-document)*