# CGPDFDictionary

**Framework**: Core Graphics

A dictionary structure within a PDF document.

#### Overview

Dictionary objects are the main building blocks of a PDF document. A key-value pair within a dictionary is called an entry. In a PDF dictionary, the key must be an array of characters. Within a given dictionary, the keys are unique—that is, no two keys in a single dictionary are equal (as determined by `strcmp`). The value associated with a key can be any kind of PDF object, including another dictionary. Dictionary objects are the main building blocks of a PDF document.

Many functions that retrieve values from a PDF dictionary take the form:

```objc
bool CGPDFDictionaryGet<DataType> (
 CGPDFDictionaryRef dictionary,
 const char *key,
 <DataType>Ref *value
);
```

These functions test whether there is an object associated with the specified key. If there is an object associated with the specified key, they test its data type. If there is no associated object, or if there is but it is not of the expected type, the function returns [`false`](https://developer.apple.com/documentation/Swift/false). If there is an object associated with the specified key and it is of the expected type, the function returns [`true`](https://developer.apple.com/documentation/Swift/true) and the object is passed back in the `value` parameter.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it. CGPDFDictionary objects exist only as constituent parts of a CGPDFDocument object, and they are managed by their container.

## Topics

### Applying a Function to All Entries
- [func CGPDFDictionaryApplyFunction(CGPDFDictionaryRef, CGPDFDictionaryApplierFunction, UnsafeMutableRawPointer?)](cgpdfdictionaryapplyfunction(_:_:_:).md)
  Applies a function to each entry in a dictionary.
### Getting Data from a Dictionary
- [func CGPDFDictionaryGetArray(CGPDFDictionaryRef, UnsafePointer<CChar>, UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](cgpdfdictionarygetarray(_:_:_:).md)
  Returns whether there is a PDF array associated with a specified key in a PDF dictionary and, if so, retrieves that array.
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
### Callbacks
- [typealias CGPDFDictionaryApplierFunction](cgpdfdictionaryapplierfunction.md)
  Performs custom processing on a key-value pair from a PDF dictionary, using optional contextual information.
### Data Types
- [struct CGPDFDictionaryRef](cgpdfdictionaryref.md)
  A type that encapsulates a PDF dictionary.

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdictionary)*