# SecCodeCopySelf(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the code object for the code making the call.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCopySelf(_ flags: SecCSFlags, _ self: UnsafeMutablePointer<SecCode?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

A code object (that is, an object of type [`SecCode`](seccode.md)) represents code that is running on the system. The code can be a UNIX process, a script, an applet, a widget, or any other separately-identifiable code. You can use the code object returned by this function as input to other functions in the Code Signing Services API. This function returns a code object for the code that calls it regardless of whether the code is signed. Call the [`SecCodeCheckValidity(_:_:_:)`](seccodecheckvalidity(_:_:_:).md) or [`SecCodeCheckValidityWithErrors(_:_:_:_:)`](seccodecheckvaliditywitherrors(_:_:_:_:).md) function to determine whether the code has a valid signature.

If the code calling this function is either a dedicated host or has called the [`SecHostSelectGuest`](sechostselectguest.md) function, then the host is considered to be acting as a proxy for its dedicated or selected guest and the [`SecCodeCopySelf(_:_:)`](seccodecopyself(_:_:).md) function returns a code object for that guest.  See [`kSecCSDedicatedHost`](kseccsdedicatedhost.md) for a discussion of dedicated hosts.

## Parameters

- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `self`: On return, a code object representing the caller.

## See Also

- [func SecCodeCopyGuestWithAttributes(SecCode?, CFDictionary?, SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyguestwithattributes(_:_:_:_:).md)
  Asks a code host to identify one of its guests given the type and value of specific attributes of the guest code.
- [func SecCodeCopyHost(SecCode, SecCSFlags, UnsafeMutablePointer<SecCode?>) -> OSStatus](seccodecopyhost(_:_:_:).md)
  Retrieves the code object for the host of specified guest code.
- [func SecCodeCopyStaticCode(SecCode, SecCSFlags, UnsafeMutablePointer<SecStaticCode?>) -> OSStatus](seccodecopystaticcode(_:_:_:).md)
  Returns a static code object representing the on-disk version of the given running code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecopyself(_:_:))*