# SecCodeCopyStaticCode(_:_:_:)

**Framework**: Security  
**Kind**: func

Returns a static code object representing the on-disk version of the given running code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCopyStaticCode(_ code: SecCode, _ flags: SecCSFlags, _ staticCode: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

Use the [`SecCodeCopyPath(_:_:_:)`](seccodecopypath(_:_:_:).md) function to get the URL specifying the location on disk of the code represented by a code or static code object.

Many functions in the Code Signing Services API take either a static code object or a code object as an input parameter. For these functions, if you pass in a code reference, the function first translates it to a static code reference in the same manner as the [`SecCodeCopyStaticCode(_:_:_:)`](seccodecopystaticcode(_:_:_:).md) function. In each such case, the parameter description documents this behavior.

##### Special Considerations

The link established by this function is generally reliable but is not guaranteed to be secure.

## Parameters

- `code`: A valid code object representing code running on the system.
- `flags`: Optional flags; see   and   for possible values. Pass   for standard behavior.
- `staticCode`: On return, a static code object representing the code in the file system that is the origin of the code specified by the   parameter.

## See Also

- [func SecCodeCopyGuestWithAttributes(SecCode?, CFDictionary?, SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyguestwithattributes(_:_:_:_:).md)
  Asks a code host to identify one of its guests given the type and value of specific attributes of the guest code.
- [func SecCodeCopyHost(SecCode, SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyhost(_:_:_:).md)
  Retrieves the code object for the host of specified guest code.
- [func SecCodeCopySelf(SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyself(_:_:).md)
  Retrieves the code object for the code making the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecopystaticcode(_:_:_:))*