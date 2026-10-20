# SecCodeCopyPath(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the location on disk of signed code, given a code or static code object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCopyPath(_ staticCode: SecStaticCode, _ flags: SecCSFlags, _ path: UnsafeMutablePointer<CFURL?>) -> OSStatus
```

```c
OSStatus SecCodeCopyPath(SecStaticCodeRef staticCode, SecCSFlags flags, CFURLRef*path);
```

#### Return Value

A result code. See [Code Signing Services Result Codes](./code-signing-services-result-codes.md).

## Parameters

- `staticCode`: The code or static code object whose code you wish to locate. If you provide a code object, the function processes it in the same manner as the  [`SecCodeCopyStaticCode(_:_:_:)`](./seccodecopystaticcode%28_,_,_%29.md) function.
- `flags`: Optional flags; see [`SecCSFlags`](./seccsflags.md) for possible values. Pass [`kSecCSDefaultFlags`](./seccsflags/kseccsdefaultflags.md) for standard behavior.
- `path`: On return, provides a URL identifying the location on disk of the code or static code object. For single files, the URL points to the file. For bundles, it points to the directory containing the entire bundle. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.

## See Also

### Related Documentation
- [func SecCodeCopySigningInformation(SecStaticCode, SecCSFlags, UnsafeMutablePointer<CFDictionary?>) -> OSStatus](./seccodecopysigninginformation%28_,_,_%29.md)
  Retrieves various pieces of information from a code signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecopypath(_:_:_:))*