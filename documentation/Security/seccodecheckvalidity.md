# SecCodeCheckValidity(_:_:_:)

**Framework**: Security  
**Kind**: func

Performs dynamic validation of signed code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCheckValidity(_ code: SecCode, _ flags: SecCSFlags, _ requirement: SecRequirement?) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

This function obtains and verifies the signature on the code specified by the code object. It checks the validity of only those sealed components required to establish identity. For guest code, first the function checks the code object’s dynamic validity status as reported by its host, then it ensures that the code object’s host is in turn valid. For all code, it validates the code against a code requirement if one is specified. The call succeeds if all these conditions are satisfactory.

This function is secure against attempts to modify the file system source of the code object.

## Parameters

- `code`: The code object to be validated.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `requirement`: A code requirement specifying additional conditions the code must satisfy to be considered valid. Specify   if you don’t want to impose any additional requirements. Use the   or   function to create a code requirement object. See   for a discussion of code requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecheckvalidity(_:_:_:))*