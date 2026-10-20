# SecStaticCodeCreateWithPathAndAttributes(_:_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a static code object representing the code at a specified file system path using an attributes dictionary.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecStaticCodeCreateWithPathAndAttributes(_ path: CFURL, _ flags: SecCSFlags, _ attributes: CFDictionary, _ staticCode: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus
```

```c
OSStatus SecStaticCodeCreateWithPathAndAttributes(CFURLRef path, SecCSFlags flags, CFDictionaryRef attributes, SecStaticCodeRef*staticCode);
```

#### Return Value

A result code. See [Code Signing Services Result Codes](./code-signing-services-result-codes.md).

#### Discussion

A static code object is not inherently linked to running code in the system.

It is possible to create a static code object from unsigned code. Although most uses of such an object cause the function to fail and return the result code [`errSecCSUnsigned`](./errseccsunsigned.md) error, you can call the [`SecCodeCopyPath(_:_:_:)`](./seccodecopypath%28_,_,_%29.md) and [`SecCodeCopySigningInformation(_:_:_:)`](./seccodecopysigninginformation%28_,_,_%29.md) functions for such objects.

## Parameters

- `path`: A URL identifying the location on disk of the code for which you want a static code object. For bundles, pass a URL to the root directory of the bundle. For single files, pass a URL to the file. If you pass a URL to the main executable of a bundle, the bundle as a whole is generally recognized. Only absolute paths should be used.
- `flags`: Optional flags; see [`SecCSFlags`](./seccsflags.md) for possible values. Pass [`kSecCSDefaultFlags`](./seccsflags/kseccsdefaultflags.md) for standard behavior.
- `attributes`: A [`CFDictionary`](../CoreFoundation/cfdictionary.md) containing additional attributes of the requested code. Possible values are defined in [Code Attributes](./code-attributes.md).
- `staticCode`: On return, the static code object representing the code you specified in the `path` parameter.

## See Also

### Related Documentation
- [func SecCodeCopyPath(SecStaticCode, SecCSFlags, UnsafeMutablePointer<CFURL?>) -> OSStatus](./seccodecopypath%28_,_,_%29.md)
  Retrieves the location on disk of signed code, given a code or static code object.
- [func SecCodeCopyStaticCode(SecCode, SecCSFlags, UnsafeMutablePointer<SecStaticCode?>) -> OSStatus](./seccodecopystaticcode%28_,_,_%29.md)
  Returns a static code object representing the on-disk version of the given running code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secstaticcodecreatewithpathandattributes(_:_:_:_:))*