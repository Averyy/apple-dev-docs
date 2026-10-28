# CGPDFDictionaryGetStream(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns whether there is a PDF stream associated with a specified key in a PDF dictionary and, if so, retrieves that stream.

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
func CGPDFDictionaryGetStream(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<CChar>, _ value: UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool
```

```c
extern bool CGPDFDictionaryGetStream(CGPDFDictionaryRef dict, const char *key, CGPDFStreamRef*value);
```

## Return Value

Returns [`true`](../Swift/true.md) if there is a PDF stream associated with the specified key; otherwise, [`false`](../Swift/false.md).

## Parameters

- `dict`: A PDF dictionary. If this parameter is not a valid PDF dictionary, the behavior is undefined.
- `key`: The key for the value to be retrieved.
- `value`: On input, a pointer to a PDF stream. If the value associated with the specified key is a PDF stream, then on return contains that stream; otherwise, the value is unspecified.

## See Also

### Getting Data from a Dictionary
- [func CGPDFDictionaryGetArray(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](./cgpdfdictionarygetarray%28_,_,_%29.md)
  Returns whether there is a PDF array associated with a specified key in a PDF dictionary and, if so, retrieves that array.
- [func CGPDFDictionaryGetBoolean(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](./cgpdfdictionarygetboolean%28_,_,_%29.md)
  Returns whether there is a PDF Boolean value associated with a specified key in a PDF dictionary and, if so, retrieves the Boolean value.
- [func CGPDFDictionaryGetCount(CGPDFDictionaryRef) -> Int](./cgpdfdictionarygetcount%28_%29.md)
  Returns the number of entries in a PDF dictionary.
- [func CGPDFDictionaryGetDictionary(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](./cgpdfdictionarygetdictionary%28_,_,_%29.md)
  Returns whether there is another PDF dictionary associated with a specified key in a PDF dictionary and, if so, retrieves that dictionary.
- [func CGPDFDictionaryGetInteger(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](./cgpdfdictionarygetinteger%28_,_,_%29.md)
  Returns whether there is a PDF integer associated with a specified key in a PDF dictionary and, if so, retrieves that integer.
- [func CGPDFDictionaryGetName(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Bool](./cgpdfdictionarygetname%28_,_,_%29.md)
  Returns whether an object with a specified key in a PDF dictionary is a PDF name reference (represented as a constant C string) and, if so, retrieves that name.
- [func CGPDFDictionaryGetNumber(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFReal>?) -> Bool](./cgpdfdictionarygetnumber%28_,_,_%29.md)
  Returns whether there is a PDF number associated with a specified key in a PDF dictionary and, if so, retrieves that number.
- [func CGPDFDictionaryGetObject(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](./cgpdfdictionarygetobject%28_,_,_%29.md)
  Returns whether there is a PDF object associated with a specified key in a PDF dictionary and, if so, retrieves that object.
- [func CGPDFDictionaryGetString(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](./cgpdfdictionarygetstring%28_,_,_%29.md)
  Returns whether there is a PDF string associated with a specified key in a PDF dictionary and, if so, retrieves that string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdictionarygetstream(_:_:_:))*