# allowsCopying

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns whether the specified PDF document allows copying.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var allowsCopying: Bool { get }
```

```c
extern bool CGPDFDocumentAllowsCopying(CGPDFDocumentRef document);
```

#### Discussion

If the document is encrypted and the current password doesn’t grant permission to perform copying, this returns [`false`](../../Swift/false.md).

## See Also

### Working with an Encrypted PDF Document
- [var isEncrypted: Bool](./isencrypted.md)
  Returns whether the specified PDF file is encrypted.
- [var allowsPrinting: Bool](./allowsprinting.md)
  Returns whether a PDF document allows printing.
- [var isUnlocked: Bool](./isunlocked.md)
  Returns whether the specified PDF document is currently unlocked.
- [func unlockWithPassword(UnsafePointer<CChar>) -> Bool](./unlockwithpassword%28_%29.md)
  Unlocks an encrypted PDF document when a valid password is supplied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/allowscopying)*