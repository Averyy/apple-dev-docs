# SecCodeCheckValidityWithErrors(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Performs dynamic validation of signed code and returns detailed error information in the case of failure.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCheckValidityWithErrors(_ code: SecCode, _ flags: SecCSFlags, _ requirement: SecRequirement?, _ errors: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

This function obtains and verifies the signature on the code specified by the code object. It checks the validity of only those sealed components required to establish identity. For guest code, first the function checks the code object’s dynamic validity status as reported by its host, then it ensures that the code object’s host is in turn valid. For all code, it validates the code against a code requirement if one is specified. The call succeeds if all these conditions are satisfactory.

This function is secure against attempts to modify the file system source of the code object.

## Parameters

- `code`: The code object to be validated.
- `flags`: Optional flags; see [`SecCSFlags`](seccsflags.md) for possible values. Pass `kSecCSDefaultFlags` for standard behavior.
- `requirement`: A code requirement specifying additional conditions the code must satisfy to be considered valid. Specify `NULL` if you don’t want to impose any additional requirements. Use the [`SecRequirementCreateWithString(_:_:_:)`](secrequirementcreatewithstring(_:_:_:).md) or [`SecRequirementCreateWithStringAndErrors(_:_:_:_:)`](secrequirementcreatewithstringanderrors(_:_:_:_:).md) function to create a code requirement object. See [`Code Signing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005929) for a discussion of code requirements.
- `errors`: On return, if the function call fails and returns a result code other than [`errSecSuccess`](errsecsuccess.md), points to an error object further describing the nature and circumstances of the failure. Use the [`CFErrorCopyUserInfo(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFErrorCopyUserInfo(_:)) function to retrieve the user info dictionary from the error object. See [`User Info Dictionary Error Keys`](user-info-dictionary-error-keys.md) for possible values. Pass `NULL` if you do not want this information. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecheckvaliditywitherrors(_:_:_:_:))*