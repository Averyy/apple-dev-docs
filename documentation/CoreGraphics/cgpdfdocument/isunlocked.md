# isUnlocked

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns whether the specified PDF document is currently unlocked.

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
var isUnlocked: Bool { get }
```

```c
extern bool CGPDFDocumentIsUnlocked(CGPDFDocumentRef document);
```

#### Discussion

There are two possible reasons why a PDF document is unlocked:

- The document is not encrypted.
- The document is encrypted, and a valid password was previously specified using [`unlockWithPassword(_:)`](./unlockwithpassword%28_%29.md).

## See Also

### Working with an Encrypted PDF Document
- [var isEncrypted: Bool](./isencrypted.md)
  Returns whether the specified PDF file is encrypted.
- [var allowsCopying: Bool](./allowscopying.md)
  Returns whether the specified PDF document allows copying.
- [var allowsPrinting: Bool](./allowsprinting.md)
  Returns whether a PDF document allows printing.
- [func unlockWithPassword(UnsafePointer<CChar>) -> Bool](./unlockwithpassword%28_%29.md)
  Unlocks an encrypted PDF document when a valid password is supplied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/isunlocked)*