# CGPDFObjectGetType(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the PDF type identifier of an object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGPDFObjectGetType(_ object: CGPDFObjectRef) -> CGPDFObjectType
```

```c
extern CGPDFObjectType CGPDFObjectGetType(CGPDFObjectRef object);
```

## Return Value

Returns the type of the `object` parameter. See [Abstract Types for PDF Document Content](./cgpdfdocument.md#Abstract-Types-for-PDF-Document-Content).

## Parameters

- `object`: A PDF object. If the value if not a PDF object, the behavior is unspecified.

## See Also

### Getting Object Types and Values
- [func CGPDFObjectGetValue(CGPDFObjectRef, CGPDFObjectType, UnsafeMutableRawPointer?) -> Bool](./cgpdfobjectgetvalue%28_,_,_%29.md)
  Returns whether an object is of a given type and if it is, retrieves its value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfobjectgettype(_:))*