# setBoolean(_:forAnnotationKey:)

**Framework**: PDFKit  
**Kind**: method

Sets a Boolean value in the annotation’s dictionary.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setBoolean(_ value: Bool, forAnnotationKey key: PDFAnnotationKey) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the value sets successfully; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `value`: The Boolean value to set in the annotation’s dictionary.
- `key`: A   or appropriate string from the Adobe PDF Specification.

## See Also

- [var annotationKeyValues: [AnyHashable : Any]](pdfannotation/annotationkeyvalues.md)
  A dictionary that contains a deep copy of the widget’s properties.
- [func value(forAnnotationKey: PDFAnnotationKey) -> Any?](pdfannotation/value(forannotationkey:).md)
  Returns a deep copy of the key-value pairs of properties for the specified key.
- [func setValue(Any, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setvalue(_:forannotationkey:).md)
  Sets a value in the annotation’s dictionary.
- [func setRect(CGRect, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setrect(_:forannotationkey:).md)
  Sets a rectangle value in the annotation’s dictionary.
- [func removeValue(forAnnotationKey: PDFAnnotationKey)](pdfannotation/removevalue(forannotationkey:).md)
  Removes a value from the annotation’s dictionary.
- [struct PDFAnnotationKey](pdfannotationkey.md)
  Keys for setting properties of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/setboolean(_:forannotationkey:))*