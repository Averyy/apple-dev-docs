# SecCodeCopySigningInformation(_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves various pieces of information from a code signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCopySigningInformation(_ code: SecStaticCode, _ flags: SecCSFlags, _ information: UnsafeMutablePointer<CFDictionary?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

The amount and detail level of the data returned is controlled by the flags passed to the call.

If the code exists but is not signed, this function call succeeds and returns a dictionary that does not contain the [`kSecCodeInfoIdentifier`](kseccodeinfoidentifier.md) key. This is the recommended way to check quickly whether code is signed if that is the only information you need. However, note that this function does not validate the signature.

If the signing data for the code is corrupt or invalid, this function may fail or it may return partial data. To ensure that only valid data is returned (and errors are raised for invalid data), you must successfully call the [`SecCodeCheckValidity(_:_:_:)`](seccodecheckvalidity(_:_:_:).md) or [`SecCodeCheckValidityWithErrors(_:_:_:_:)`](seccodecheckvaliditywitherrors(_:_:_:_:).md) function before calling [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md).

##### Special Considerations

Some of the objects returned in the information dictionary are (retained) “live” API objects used by the code signing infrastructure. Making changes to these objects is unsupported and may cause subsequent code signing operations on the affected code to behave in undefined ways.

## Parameters

- `code`: The code or static code object from whose signature you wish to retrieve information. If you provide a code object, the function processes it in the same manner as the   function—that is, the static code signing information is obtained from the signature on disk. Note that dynamic information ( ) can be obtained only for a code object, not for a static code object.
- `flags`: Specify any or all of the flags in   to select what information to return. A basic set of values is returned regardless; specify   for just those.
- `information`: On return, a dictionary containing information about the code. The contents of the dictionary depend on the flags you pass in the   parameter. Regardless of flags, the   key is always present if the code is signed and always absent if the code is unsigned. See   for descriptions of the dictionary keys.  In Objective-C, call the   function to release this object when you are finished with it.

## See Also

- [func SecCodeCopyDesignatedRequirement(SecStaticCode, SecCSFlags, UnsafeMutablePointer<SecRequirement?>) -> OSStatus](seccodecopydesignatedrequirement(_:_:_:).md)
  Retrieves the designated code requirement of signed code.
- [func SecCodeCopyPath(SecStaticCode, SecCSFlags, UnsafeMutablePointer<CFURL?>) -> OSStatus](seccodecopypath(_:_:_:).md)
  Retrieves the location on disk of signed code, given a code or static code object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecopysigninginformation(_:_:_:))*