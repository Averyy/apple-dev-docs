# isUnlocked

**Framework**: Core Graphics  
**Kind**: property

Returns whether the specified PDF document is currently unlocked.

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
var isUnlocked: Bool { get }
```

#### Discussion

There are two possible reasons why a PDF document is unlocked:

- The document is not encrypted.
- The document is encrypted, and a valid password was previously specified using [`unlockWithPassword(_:)`](cgpdfdocument/unlockwithpassword(_:).md).

## See Also

- [var isEncrypted: Bool](cgpdfdocument/isencrypted.md)
  Returns whether the specified PDF file is encrypted.
- [var allowsCopying: Bool](cgpdfdocument/allowscopying.md)
  Returns whether the specified PDF document allows copying.
- [var allowsPrinting: Bool](cgpdfdocument/allowsprinting.md)
  Returns whether a PDF document allows printing.
- [func unlockWithPassword(UnsafePointer<CChar>) -> Bool](cgpdfdocument/unlockwithpassword(_:).md)
  Unlocks an encrypted PDF document when a valid password is supplied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/isunlocked)*