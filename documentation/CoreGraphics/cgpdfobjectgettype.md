# CGPDFObjectGetType(_:)

**Framework**: Core Graphics  
**Kind**: func

Returns the PDF type identifier of an object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFObjectGetType(_ object: CGPDFObjectRef) -> CGPDFObjectType
```

#### Return Value

Returns the type of the `object` parameter. See [`Abstract Types for PDF Document Content`](cgpdfdocument#Abstract-Types-for-PDF-Document-Content.md).

## Parameters

- `object`: A PDF object. If the value if not a PDF object, the behavior is unspecified.

## See Also

- [func CGPDFObjectGetValue(CGPDFObjectRef, CGPDFObjectType, UnsafeMutableRawPointer?) -> Bool](cgpdfobjectgetvalue(_:_:_:).md)
  Returns whether an object is of a given type and if it is, retrieves its value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfobjectgettype(_:))*