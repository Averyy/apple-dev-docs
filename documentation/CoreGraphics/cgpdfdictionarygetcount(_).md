# CGPDFDictionaryGetCount(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the number of entries in a PDF dictionary.

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
func CGPDFDictionaryGetCount(_ dict: CGPDFDictionaryRef) -> Int
```

```c
extern size_t CGPDFDictionaryGetCount(CGPDFDictionaryRef dict);
```

## Return Value

Returns the number of entries in the dictionary.

## Parameters

- `dict`: A PDF dictionary. If this parameter is not a valid PDF dictionary, the behavior is undefined.

## See Also

### Getting Data from a Dictionary
- [func CGPDFDictionaryGetArray(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](./cgpdfdictionarygetarray%28_,_,_%29.md)
  Returns whether there is a PDF array associated with a specified key in a PDF dictionary and, if so, retrieves that array.
- [func CGPDFDictionaryGetBoolean(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](./cgpdfdictionarygetboolean%28_,_,_%29.md)
  Returns whether there is a PDF Boolean value associated with a specified key in a PDF dictionary and, if so, retrieves the Boolean value.
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
- [func CGPDFDictionaryGetStream(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](./cgpdfdictionarygetstream%28_,_,_%29.md)
  Returns whether there is a PDF stream associated with a specified key in a PDF dictionary and, if so, retrieves that stream.
- [func CGPDFDictionaryGetString(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](./cgpdfdictionarygetstring%28_,_,_%29.md)
  Returns whether there is a PDF string associated with a specified key in a PDF dictionary and, if so, retrieves that string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdictionarygetcount(_:))*