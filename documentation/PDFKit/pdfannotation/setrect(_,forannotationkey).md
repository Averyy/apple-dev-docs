# setRect(_:forAnnotationKey:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Sets a rectangle value in the annotation’s dictionary.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func setRect(_ value: CGRect, forAnnotationKey key: PDFAnnotationKey) -> Bool
```

*macOS*

```swift
func setRect(_ value: NSRect, forAnnotationKey key: PDFAnnotationKey) -> Bool
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (BOOL) setRect:(CGRect) value forAnnotationKey:(PDFAnnotationKey) key;
```

*macOS*

```objc
- (BOOL) setRect:(NSRect) value forAnnotationKey:(PDFAnnotationKey) key;
```

#### Return Value

[`true`](../../Swift/true.md) if the value sets successfully; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `value`: The rectangle value to set in the annotation’s dictionary.
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
- [func removeValue(forAnnotationKey: PDFAnnotationKey)](./removevalue%28forannotationkey%29.md)
  Removes a value from the annotation’s dictionary.
- [struct PDFAnnotationKey](../pdfannotationkey.md)
  Keys for setting properties of annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/setrect(_:forannotationkey:))*