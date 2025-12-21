# CGPDFDictionaryGetArray(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Returns whether there is a PDF array associated with a specified key in a PDF dictionary and, if so, retrieves that array.

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
func CGPDFDictionaryGetArray(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<CChar>, _ value: UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if there is a PDF array associated with the specified key; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `dict`: A PDF dictionary. If this parameter is not a valid PDF dictionary, the behavior is undefined.
- `key`: The key for the value to retrieve.
- `value`: On input, an uninitialized pointer to a PDF array. If the value associated with the specified key is a PDF array, then on return contains that array; otherwise the value is unspecified.

## See Also

- [func CGPDFDictionaryGetBoolean(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](cgpdfdictionarygetboolean(_:_:_:).md)
  Returns whether there is a PDF Boolean value associated with a specified key in a PDF dictionary and, if so, retrieves the Boolean value.
- [func CGPDFDictionaryGetCount(CGPDFDictionaryRef) -> Int](cgpdfdictionarygetcount(_:).md)
  Returns the number of entries in a PDF dictionary.
- [func CGPDFDictionaryGetDictionary(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](cgpdfdictionarygetdictionary(_:_:_:).md)
  Returns whether there is another PDF dictionary associated with a specified key in a PDF dictionary and, if so, retrieves that dictionary.
- [func CGPDFDictionaryGetInteger(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](cgpdfdictionarygetinteger(_:_:_:).md)
  Returns whether there is a PDF integer associated with a specified key in a PDF dictionary and, if so, retrieves that integer.
- [func CGPDFDictionaryGetName(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Bool](cgpdfdictionarygetname(_:_:_:).md)
  Returns whether an object with a specified key in a PDF dictionary is a PDF name reference (represented as a constant C string) and, if so, retrieves that name.
- [func CGPDFDictionaryGetNumber(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFReal>?) -> Bool](cgpdfdictionarygetnumber(_:_:_:).md)
  Returns whether there is a PDF number associated with a specified key in a PDF dictionary and, if so, retrieves that number.
- [func CGPDFDictionaryGetObject(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](cgpdfdictionarygetobject(_:_:_:).md)
  Returns whether there is a PDF object associated with a specified key in a PDF dictionary and, if so, retrieves that object.
- [func CGPDFDictionaryGetStream(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](cgpdfdictionarygetstream(_:_:_:).md)
  Returns whether there is a PDF stream associated with a specified key in a PDF dictionary and, if so, retrieves that stream.
- [func CGPDFDictionaryGetString(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](cgpdfdictionarygetstring(_:_:_:).md)
  Returns whether there is a PDF string associated with a specified key in a PDF dictionary and, if so, retrieves that string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdictionarygetarray(_:_:_:))*