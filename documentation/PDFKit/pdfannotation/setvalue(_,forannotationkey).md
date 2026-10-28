# setValue(_:forAnnotationKey:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) setValue:(id) value forAnnotationKey:(PDFAnnotationKey) key;
```

## Return Value

[`true`](../../Swift/true.md) if the value sets successfully; otherwise, [`false`](../../Swift/false.md).

## Discussion

Some keys expect a complex type. For example, the [`color`](../pdfannotationkey/color.md) key expects an array of zero, one, two, three, or four elements, where each element is a floating-point number from `0.0` to `1.0`. As a convenience, this key accepts an [`NSColor`](../../AppKit/nscolor.md) or [`UIColor`](../../UIKit/uicolor.md) value. For details about other conveniences, see the individual [`PDFAnnotationKey`](../pdfannotationkey.md) properties or the `PDFAnnotationUtilities.h` header file.

> 💡 **Tip**:  Set the `PDFKIT_LOG_ANNOTATIONS` environment variable to log key-value assignment failure details.

## Parameters

- `value`: The value to set in the attribute’s dictionary.
- `key`: A [`PDFAnnotationKey`](../pdfannotationkey.md) or appropriate string from the Adobe PDF Specification.

## See Also

### Modifying Annotation Attributes
- [var annotationKeyValues: [AnyHashable : Any]](./annotationkeyvalues.md)
  A dictionary that contains a deep copy of the widget’s properties.
- [func value(forAnnotationKey: PDFAnnotationKey) -> Any?](./value%28forannotationkey%29.md)
  Returns a deep copy of the key-value pairs of properties for the specified key.
- [func setBoolean(Bool, forAnnotationKey: PDFAnnotationKey) -> Bool](./setboolean%28_,forannotationkey%29.md)
  Sets a Boolean value in the annotation’s dictionary.
- [func setRect(CGRect, forAnnotationKey: PDFAnnotationKey) -> Bool](./setrect%28_,forannotationkey%29.md)
  Sets a rectangle value in the annotation’s dictionary.
- [func removeValue(forAnnotationKey: PDFAnnotationKey)](./removevalue%28forannotationkey%29.md)
  Removes a value from the annotation’s dictionary.
- [struct PDFAnnotationKey](../pdfannotationkey.md)
  Keys for setting properties of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/setvalue(_:forannotationkey:))*