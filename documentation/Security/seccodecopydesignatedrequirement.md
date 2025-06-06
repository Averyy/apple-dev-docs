# SecCodeCopyDesignatedRequirement(_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the designated code requirement of signed code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCopyDesignatedRequirement(_ code: SecStaticCode, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

The designated requirement is the internal code requirement that the code specifies as the way to identify it. See [`Code Signing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005929) for a discussion of code requirements and designated requirements.

If the code contains an explicit designated requirement, a copy of that is returned. If it doesn’t, a designated requirement is constructed from the code’s signing authority and its embedded unique identifier. No designated requirement can be obtained from unsigned code. Code that is modified after being signed, that has been signed improperly, or whose signature has become invalid, may or may not yield a designated requirement. This function does not validate the signature.

## Parameters

- `code`: The code or static code object for which you want the designated requirement. If you provide a code object, the function processes it in the same manner as the    function.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `requirement`: On return, the code’s designated requirement. In Objective-C, call the   function to release this object when you are finished with it.

## See Also

- [func SecCodeCopySigningInformation(SecStaticCode, SecCSFlags, UnsafeMutablePointer<CFDictionary?>) -> OSStatus](seccodecopysigninginformation(_:_:_:).md)
  Retrieves various pieces of information from a code signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecopydesignatedrequirement(_:_:_:))*