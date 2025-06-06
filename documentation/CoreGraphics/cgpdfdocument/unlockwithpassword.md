# unlockWithPassword(_:)

**Framework**: Core Graphics  
**Kind**: method

Unlocks an encrypted PDF document when a valid password is supplied.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func unlockWithPassword(_ password: UnsafePointer<CChar>) -> Bool
```

#### Return Value

A Boolean that, if [`true`](https://developer.apple.com/documentation/swift/true), indicates that the document has been successfully unlocked. If the value is [`false`](https://developer.apple.com/documentation/swift/false), the document has not been unlocked.

#### Discussion

Given an encrypted PDF document and a password, this function does the following:

- Sets the lock state of the document, based on the validity of the password.
- Returns [`true`](https://developer.apple.com/documentation/swift/true) if the document is unlocked.
- Returns [`false`](https://developer.apple.com/documentation/swift/false) if the document cannot be unlocked with the specified password.

Unlocking a PDF document makes it possible to decrypt the document and perform other privileged operations. Different passwords enable different operations.

## Parameters

- `password`: A pointer to a string that contains the password.

## See Also

- [var isEncrypted: Bool](cgpdfdocument/isencrypted.md)
  Returns whether the specified PDF file is encrypted.
- [var allowsCopying: Bool](cgpdfdocument/allowscopying.md)
  Returns whether the specified PDF document allows copying.
- [var allowsPrinting: Bool](cgpdfdocument/allowsprinting.md)
  Returns whether a PDF document allows printing.
- [var isUnlocked: Bool](cgpdfdocument/isunlocked.md)
  Returns whether the specified PDF document is currently unlocked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/unlockwithpassword(_:))*