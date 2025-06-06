# isEncrypted

**Framework**: Core Graphics  
**Kind**: property

Returns whether the specified PDF file is encrypted.

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
var isEncrypted: Bool { get }
```

#### Discussion

If the document is encrypted, a password must be supplied before certain operations are enabled. For more information, see [`unlockWithPassword(_:)`](cgpdfdocument/unlockwithpassword(_:).md).

## See Also

- [var allowsCopying: Bool](cgpdfdocument/allowscopying.md)
  Returns whether the specified PDF document allows copying.
- [var allowsPrinting: Bool](cgpdfdocument/allowsprinting.md)
  Returns whether a PDF document allows printing.
- [var isUnlocked: Bool](cgpdfdocument/isunlocked.md)
  Returns whether the specified PDF document is currently unlocked.
- [func unlockWithPassword(UnsafePointer<CChar>) -> Bool](cgpdfdocument/unlockwithpassword(_:).md)
  Unlocks an encrypted PDF document when a valid password is supplied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/isencrypted)*