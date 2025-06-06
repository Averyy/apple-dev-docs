# SecRequirementCreateWithString(_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a code requirement object by compiling a valid text representation of a code requirement.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecRequirementCreateWithString(_ text: CFString, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

Code requirements and the code signing requirement language are documented in [`Code Signing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40005929).

If you use the [`SecRequirementCreateWithString(_:_:_:)`](secrequirementcreatewithstring(_:_:_:).md) function to create a code requirement object from a text string and later use the [`SecRequirementCopyString(_:_:_:)`](secrequirementcopystring(_:_:_:).md) function to convert the object back to a string, the reconstituted text may differ in formatting, contain different source comments, and perform its validation functions in different order from the original. However, it is guaranteed that that the reconstituted text is functionally identical to the original. That is, recompiling the text using [`SecRequirementCreateWithString(_:_:_:)`](secrequirementcreatewithstring(_:_:_:).md) will produce a code requirement object that behaves identically to the first one you created.

## Parameters

- `text`: The text form of a code requirement.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `requirement`: On return, contains a code requirement object that implements the conditions described in the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrequirementcreatewithstring(_:_:_:))*