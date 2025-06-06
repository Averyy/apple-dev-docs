# SecStaticCodeCheckValidityWithErrors(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Performs static validation of static signed code and returns detailed error information in the case of failure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecStaticCodeCheckValidityWithErrors(_ staticCode: SecStaticCode, _ flags: SecCSFlags, _ requirement: SecRequirement?, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

This function obtains and verifies the signature on the code specified by the code object. It checks the validity of all sealed components, including resources (if any). It validates the code against a code requirement if one is specified. The call succeeds if all these conditions are satisfactory.

This call is only secure if the code is not subject to concurrent modification, and the outcome is only valid as long as the code remains unmodified. If the underlying file system has dynamic characteristics, such as a network file system, union mount, or FUSE, you must consider how secure the code is from modification after validation.

When checking a universal binary, include the [`kSecCSCheckAllArchitectures`](kseccscheckallarchitectures.md) flag. Otherwise the method verifies only one slice of the binary, potentially indicating success without testing all the slices. Be aware that the slices of a universal binary don’t have to be signed by the same signer for the test to pass. One slice might be ad hoc signed, for example. But the validity check doesn’t know which slice you are going to run. For example, the user might use the arch(1) command line utility to pick a 32-bit architecture even though a 64-bit architecture is available.

If you want to be sure to test a particular slice, create the static code object with the [`SecStaticCodeCreateWithPathAndAttributes(_:_:_:_:)`](secstaticcodecreatewithpathandattributes(_:_:_:_:).md) method using the [`kSecCodeAttributeArchitecture`](kseccodeattributearchitecture.md) and [`kSecCodeAttributeSubarchitecture`](kseccodeattributesubarchitecture.md) attributes (if you know the architecture) or the [`kSecCodeAttributeUniversalFileOffset`](kseccodeattributeuniversalfileoffset.md) attribute (if you know the offset into the universal binary).

## Parameters

- `staticCode`: The code object to be validated.
- `flags`: Optional flags; see   for possible values. Use   to validate all slices of a universal binary.
- `requirement`: A code requirement specifying additional conditions the code must satisfy to be considered valid. Specify   if you don’t want to impose any additional requirements. Use the   or   function to create a code requirement object. See   for a discussion of code requirements.
- `errors`: On return, if the function call fails and returns a result code other than  , points to an error object further describing the nature and circumstances of the failure. Use the   function to retrieve the user info dictionary from the error object. See   for possible values. Pass   if you do not want this information. Call the   function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secstaticcodecheckvaliditywitherrors(_:_:_:_:))*