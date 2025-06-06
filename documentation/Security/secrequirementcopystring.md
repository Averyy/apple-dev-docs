# SecRequirementCopyString(_:_:_:)

**Framework**: Security  
**Kind**: func

Converts a code requirement object into text form.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecRequirementCopyString(_ requirement: SecRequirement, _ flags: SecCSFlags, _ text: UnsafeMutablePointer<CFString?>) -> OSStatus
```

#### Return Value

A result code. See [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

#### Discussion

If you use the [`SecRequirementCreateWithString(_:_:_:)`](secrequirementcreatewithstring(_:_:_:).md) or [`SecRequirementCreateWithStringAndErrors(_:_:_:_:)`](secrequirementcreatewithstringanderrors(_:_:_:_:).md) function to create a code requirement object from a text string and later use the [`SecRequirementCopyString(_:_:_:)`](secrequirementcopystring(_:_:_:).md) function to convert the object back to a string, the reconstituted text may differ in formatting, contain different source comments, and perform its validation functions in different order from the original. However, it is guaranteed that that the reconstituted text is functionally identical to the original. That is, recompiling the text using [`SecRequirementCreateWithString(_:_:_:)`](secrequirementcreatewithstring(_:_:_:).md) will produce a code requirement object that behaves identically to the first one you created.

## Parameters

- `requirement`: A valid code requirement object.
- `flags`: Optional flags; see   for possible values. Pass   for standard behavior.
- `text`: On return, a text representation of the code requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrequirementcopystring(_:_:_:))*