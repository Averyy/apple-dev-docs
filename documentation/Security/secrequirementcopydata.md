# SecRequirementCopyData(_:_:_:)

**Framework**: Security  
**Kind**: func

Extracts a binary form of a code requirement from a code requirement object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecRequirementCopyData(_ requirement: SecRequirement, _ flags: SecCSFlags, _ data: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

You can extract the binary blob from the [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object and store it in any form you wish. Use of this function is the only publicly supported way to get such a data blob. You can use the [`SecRequirementCreateWithData(_:_:_:)`](secrequirementcreatewithdata(_:_:_:).md) function to convert it back to a code requirement object.

## Parameters

- `requirement`: A valid code requirement object.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `data`: On return, the code requirement in the form of a binary blob.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrequirementcopydata(_:_:_:))*