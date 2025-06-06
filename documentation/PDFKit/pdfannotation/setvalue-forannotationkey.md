# setValue(_:forAnnotationKey:)

**Framework**: PDFKit  
**Kind**: method

Sets a value in the annotation’s dictionary.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: Any, forAnnotationKey key: PDFAnnotationKey) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the value sets successfully; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Some keys expect a complex type. For example, the [`color`](pdfannotationkey/color.md) key expects an array of zero, one, two, three, or four elements, where each element is a floating-point number from `0.0` to `1.0`. As a convenience, this key accepts an [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) or [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) value. For details about other conveniences, see the individual [`PDFAnnotationKey`](pdfannotationkey.md) properties or the `PDFAnnotationUtilities.h` header file.

> 💡 **Tip**:  Set the `PDFKIT_LOG_ANNOTATIONS` environment variable to log key-value assignment failure details.

 Set the `PDFKIT_LOG_ANNOTATIONS` environment variable to log key-value assignment failure details.

## Parameters

- `value`: The value to set in the attribute’s dictionary.
- `key`: A   or appropriate string from the Adobe PDF Specification.

## See Also

- [var annotationKeyValues: [AnyHashable : Any]](pdfannotation/annotationkeyvalues.md)
  A dictionary that contains a deep copy of the widget’s properties.
- [func value(forAnnotationKey: PDFAnnotationKey) -> Any?](pdfannotation/value(forannotationkey:).md)
  Returns a deep copy of the key-value pairs of properties for the specified key.
- [func setBoolean(Bool, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setboolean(_:forannotationkey:).md)
  Sets a Boolean value in the annotation’s dictionary.
- [func setRect(CGRect, forAnnotationKey: PDFAnnotationKey) -> Bool](pdfannotation/setrect(_:forannotationkey:).md)
  Sets a rectangle value in the annotation’s dictionary.
- [func removeValue(forAnnotationKey: PDFAnnotationKey)](pdfannotation/removevalue(forannotationkey:).md)
  Removes a value from the annotation’s dictionary.
- [struct PDFAnnotationKey](pdfannotationkey.md)
  Keys for setting properties of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/setvalue(_:forannotationkey:))*