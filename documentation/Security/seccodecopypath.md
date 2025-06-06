# SecCodeCopyPath(_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the location on disk of signed code, given a code or static code object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCopyPath(_ staticCode: SecStaticCode, _ flags: SecCSFlags, _ path: UnsafeMutablePointer<CFURL?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

## Parameters

- `staticCode`: The code or static code object whose code you wish to locate. If you provide a code object, the function processes it in the same manner as the    function.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `path`: On return, provides a URL identifying the location on disk of the code or static code object. For single files, the URL points to the file. For bundles, it points to the directory containing the entire bundle. In Objective-C, call the   function to release this object when you are finished with it.

## See Also

- [func SecCodeCopySigningInformation(SecStaticCode, SecCSFlags, UnsafeMutablePointer<CFDictionary?>) -> OSStatus](seccodecopysigninginformation(_:_:_:).md)
  Retrieves various pieces of information from a code signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecopypath(_:_:_:))*