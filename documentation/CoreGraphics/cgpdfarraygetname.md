# CGPDFArrayGetName(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func

Returns whether an object at a given index in a PDF array is a PDF name reference (represented as a constant C string) and, if so, retrieves that name.

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
func CGPDFArrayGetName(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if there is an array of characters at the specified index, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `array`: A PDF array. If this parameter is not a valid PDF array, the behavior is undefined.
- `index`: The index of the value to retrieve. If the index is outside the index space of the array (  to  , where   is the count of the array), the behavior is undefined.
- `value`: An uninitialized pointer to a constant C string. If the value at the specified index is a reference to a PDF name (represented by a constant C string) then upon return, contains that value; otherwise the value is undefined.

## See Also

- [func CGPDFArrayGetArray(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](cgpdfarraygetarray(_:_:_:).md)
  Returns whether an object at a given index in a PDF array is another PDF array and, if so, retrieves that array.
- [func CGPDFArrayGetBoolean(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](cgpdfarraygetboolean(_:_:_:).md)
  Returns whether an object at a given index in a PDF array is a PDF Boolean and, if so, retrieves that Boolean.
- [func CGPDFArrayGetCount(CGPDFArrayRef) -> Int](cgpdfarraygetcount(_:).md)
  Returns the number of items in a PDF array.
- [func CGPDFArrayGetDictionary(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](cgpdfarraygetdictionary(_:_:_:).md)
  Returns whether an object at a given index in a PDF array is a PDF dictionary and, if so, retrieves that dictionary.
- [func CGPDFArrayGetInteger(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](cgpdfarraygetinteger(_:_:_:).md)
  Returns whether an object at a given index in a PDF array is a PDF integer and, if so, retrieves that object.
- [func CGPDFArrayGetNull(CGPDFArrayRef, Int) -> Bool](cgpdfarraygetnull(_:_:).md)
  Returns whether an object at a given index in a Quartz PDF array is a PDF null.
- [func CGPDFArrayGetNumber(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFReal>?) -> Bool](cgpdfarraygetnumber(_:_:_:).md)
  Returns whether an object at a given index in a PDF array is a PDF number and, if so, retrieves that object.
- [func CGPDFArrayGetObject(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](cgpdfarraygetobject(_:_:_:).md)
  Returns whether an object at a given index in a PDF array is a PDF object and, if so, retrieves that object.
- [func CGPDFArrayGetStream(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](cgpdfarraygetstream(_:_:_:).md)
  Returns whether an object at a given index in a PDF array is a PDF stream and, if so, retrieves that stream.
- [func CGPDFArrayGetString(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](cgpdfarraygetstring(_:_:_:).md)
  Returns whether an object at a given index in a PDF array is a PDF string and, if so, retrieves that string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfarraygetname(_:_:_:))*