# SecRequirementCreateWithData(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a code requirement object from the binary form of a code requirement.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecRequirementCreateWithData(_ data: CFData, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus
```

```c
OSStatus SecRequirementCreateWithData(CFDataRef data, SecCSFlags flags, SecRequirementRef*requirement);
```

## Return Value

A result code. See [Code Signing Services Result Codes](./code-signing-services-result-codes.md).

## Discussion

You can use the [`SecRequirementCopyData(_:_:_:)`](./secrequirementcopydata%28_,_,_%29.md) function to convert a code requirement object to a binary blob, and store the blob in any form you wish. When you are ready to use the code requirement in another function call, you can use the [`SecRequirementCreateWithData(_:_:_:)`](./secrequirementcreatewithdata%28_,_,_%29.md) function to convert it back to a code requirement object.

## Parameters

- `data`: A binary blob created earlier from a valid code requirement object by calling the [`SecRequirementCopyData(_:_:_:)`](./secrequirementcopydata%28_,_,_%29.md) function.
- `flags`: Optional flags; see [`SecCSFlags`](./seccsflags.md) for possible values. Pass [`kSecCSDefaultFlags`](./seccsflags/kseccsdefaultflags.md) for standard behavior.
- `requirement`: On return, contains a code requirement object that behaves identically to the one from which the data blob was obtained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrequirementcreatewithdata(_:_:_:))*