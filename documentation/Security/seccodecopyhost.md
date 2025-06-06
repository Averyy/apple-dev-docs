# SecCodeCopyHost(_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the code object for the host of specified guest code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecCodeCopyHost(_ guest: SecCode, _ flags: SecCSFlags, _ host: UnsafeMutablePointer<SecCode?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

Host code acts as the supervisor and controller of its guest code and is the ultimate authority on the dynamic validity and status of its guests.

## Parameters

- `guest`: A valid code object representing code running on the system as the guest of other code.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `host`: On return, the code object of the host of the code specified in the   parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodecopyhost(_:_:_:))*