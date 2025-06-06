# SecCodeMapMemory(_:_:)

**Framework**: Security  
**Kind**: func

Asks the kernel to accept the signing information currently attached to a code object and uses it to validate memory page-ins.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeMapMemory(_ code: SecStaticCode, _ flags: SecCSFlags) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

This function is for the use of code hosts that use memory mapping to manage their own code. The kernel takes the signing information attached to the code on disk specified by the `code` parameter and attaches it to the memory object. After that, it uses the signature to validate memory page-ins, updating the dynamic validity status accordingly. You can use the [`SecCodeCopySigningInformation(_:_:_:)`](seccodecopysigninginformation(_:_:_:).md) function to check the code’s dynamic validity status. The attachment of the signature to the memory object affects all processes that have the main executable of this code mapped.

## Parameters

- `code`: A code or static code object representing the signed code whose main executable should be subject to page-in validation. If you provide a code object, the function processes it in the same manner as the    function—that is, whether you provide a code object or a static code object, the function actually takes the signature from the code on disk.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodemapmemory(_:_:))*