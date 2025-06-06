# annotationKeyValues

**Framework**: PDFKit  
**Kind**: property

A dictionary that contains a deep copy of the widget’s properties.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var annotationKeyValues: [AnyHashable : Any] { get }
```

## See Also

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
- [struct PDFAnnotationKey](pdfannotationkey.md)
  Keys for setting properties of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/annotationkeyvalues)*