# SecRequirementCreateWithData(_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a code requirement object from the binary form of a code requirement.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecRequirementCreateWithData(_ data: CFData, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

You can use the [`SecRequirementCopyData(_:_:_:)`](secrequirementcopydata(_:_:_:).md) function to convert a code requirement object to a binary blob, and store the blob in any form you wish. When you are ready to use the code requirement in another function call, you can use the [`SecRequirementCreateWithData(_:_:_:)`](secrequirementcreatewithdata(_:_:_:).md) function to convert it back to a code requirement object.

## Parameters

- `data`: A binary blob created earlier from a valid code requirement object by calling the   function.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `requirement`: On return, contains a code requirement object that behaves identically to the one from which the data blob was obtained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrequirementcreatewithdata(_:_:_:))*