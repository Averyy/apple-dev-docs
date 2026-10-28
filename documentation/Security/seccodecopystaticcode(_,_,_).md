# SecCodeCopyStaticCode(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns a static code object representing the on-disk version of the given running code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCopyStaticCode(_ code: SecCode, _ flags: SecCSFlags, _ staticCode: UnsafeMutablePointer<SecStaticCode?>) -> OSStatus
```

```c
OSStatus SecCodeCopyStaticCode(SecCodeRef code, SecCSFlags flags, SecStaticCodeRef*staticCode);
```

## Return Value

A result code. See [Code Signing Services Result Codes](./code-signing-services-result-codes.md).

## Discussion

Use the [`SecCodeCopyPath(_:_:_:)`](./seccodecopypath%28_,_,_%29.md) function to get the URL specifying the location on disk of the code represented by a code or static code object.

Many functions in the Code Signing Services API take either a static code object or a code object as an input parameter. For these functions, if you pass in a code reference, the function first translates it to a static code reference in the same manner as the [`SecCodeCopyStaticCode(_:_:_:)`](./seccodecopystaticcode%28_,_,_%29.md) function. In each such case, the parameter description documents this behavior.

### Special Considerations

The link established by this function is generally reliable but is not guaranteed to be secure.

## Parameters

- `code`: A valid code object representing code running on the system.
- `flags`: Optional flags; see [`SecCSFlags`](./seccsflags.md) and [Code Signing Architecture Flags](./code-signing-architecture-flags.md) for possible values. Pass [`kSecCSDefaultFlags`](./seccsflags/kseccsdefaultflags.md) for standard behavior.
- `staticCode`: On return, a static code object representing the code in the file system that is the origin of the code specified by the `code` parameter.

## See Also

### Related Documentation
- [func SecCodeCopyGuestWithAttributes(SecCode?, CFDictionary?, SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](./seccodecopyguestwithattributes%28_,_,_,_%29.md)
  Asks a code host to identify one of its guests given the type and value of specific attributes of the guest code.
- [func SecCodeCopyHost(SecCode, SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](./seccodecopyhost%28_,_,_%29.md)
  Retrieves the code object for the host of specified guest code.
- [func SecCodeCopySelf(SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](./seccodecopyself%28_,_%29.md)
  Retrieves the code object for the code making the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecopystaticcode(_:_:_:))*