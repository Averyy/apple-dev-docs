# CGPDFArrayGetCount(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the number of items in a PDF array.

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
func CGPDFArrayGetCount(_ array: CGPDFArrayRef) -> Int
```

```c
extern size_t CGPDFArrayGetCount(CGPDFArrayRef array);
```

#### Return Value

Returns the number of items in the array.

## Parameters

- `array`: A PDF array. If this parameter is not a valid PDF array, the behavior is undefined.

## See Also

### Getting Data from a PDF Array
- [func CGPDFArrayGetArray(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](./cgpdfarraygetarray%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is another PDF array and, if so, retrieves that array.
- [func CGPDFArrayGetBoolean(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](./cgpdfarraygetboolean%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF Boolean and, if so, retrieves that Boolean.
- [func CGPDFArrayGetDictionary(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](./cgpdfarraygetdictionary%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF dictionary and, if so, retrieves that dictionary.
- [func CGPDFArrayGetInteger(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFInteger>?) -> Bool](./cgpdfarraygetinteger%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF integer and, if so, retrieves that object.
- [func CGPDFArrayGetName(CGPDFArrayRef, Int, UnsafeMutablePointer<UnsafePointer<CChar>?>?) -> Bool](./cgpdfarraygetname%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF name reference (represented as a constant C string) and, if so, retrieves that name.
- [func CGPDFArrayGetNull(CGPDFArrayRef, Int) -> Bool](./cgpdfarraygetnull%28_,_%29.md)
  Returns whether an object at a given index in a Quartz PDF array is a PDF null.
- [func CGPDFArrayGetNumber(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFReal>?) -> Bool](./cgpdfarraygetnumber%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF number and, if so, retrieves that object.
- [func CGPDFArrayGetObject(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](./cgpdfarraygetobject%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF object and, if so, retrieves that object.
- [func CGPDFArrayGetStream(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](./cgpdfarraygetstream%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF stream and, if so, retrieves that stream.
- [func CGPDFArrayGetString(CGPDFArrayRef, Int, UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](./cgpdfarraygetstring%28_,_,_%29.md)
  Returns whether an object at a given index in a PDF array is a PDF string and, if so, retrieves that string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfarraygetcount(_:))*