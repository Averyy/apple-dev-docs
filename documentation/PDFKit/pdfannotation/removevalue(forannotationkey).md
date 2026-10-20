# removeValue(forAnnotationKey:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Removes a value from the annotation’s dictionary.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeValue(forAnnotationKey key: PDFAnnotationKey)
```

```objc
- (void) removeValueForAnnotationKey:(PDFAnnotationKey) key;
```

## Parameters

- `key`: A [`PDFAnnotationKey`](../pdfannotationkey.md) or appropriate string from the Adobe PDF Specification.

## See Also

### Modifying Annotation Attributes
- [var annotationKeyValues: [AnyHashable : Any]](./annotationkeyvalues.md)
  A dictionary that contains a deep copy of the widget’s properties.
- [func value(forAnnotationKey: PDFAnnotationKey) -> Any?](./value%28forannotationkey%29.md)
  Returns a deep copy of the key-value pairs of properties for the specified key.
- [func setValue(Any, forAnnotationKey: PDFAnnotationKey) -> Bool](./setvalue%28_,forannotationkey%29.md)
  Sets a value in the annotation’s dictionary.
- [func setBoolean(Bool, forAnnotationKey: PDFAnnotationKey) -> Bool](./setboolean%28_,forannotationkey%29.md)
  Sets a Boolean value in the annotation’s dictionary.
- [func setRect(CGRect, forAnnotationKey: PDFAnnotationKey) -> Bool](./setrect%28_,forannotationkey%29.md)
  Sets a rectangle value in the annotation’s dictionary.
- [struct PDFAnnotationKey](../pdfannotationkey.md)
  Keys for setting properties of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/removevalue(forannotationkey:))*