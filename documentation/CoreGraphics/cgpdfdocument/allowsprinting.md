# allowsPrinting

**Framework**: Core Graphics  
**Kind**: property

Returns whether a PDF document allows printing.

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
var allowsPrinting: Bool { get }
```

#### Discussion

If the document is encrypted and the current password doesn’t grant permission to perform printing, this returns [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isEncrypted: Bool](cgpdfdocument/isencrypted.md)
  Returns whether the specified PDF file is encrypted.
- [var allowsCopying: Bool](cgpdfdocument/allowscopying.md)
  Returns whether the specified PDF document allows copying.
- [var isUnlocked: Bool](cgpdfdocument/isunlocked.md)
  Returns whether the specified PDF document is currently unlocked.
- [func unlockWithPassword(UnsafePointer<CChar>) -> Bool](cgpdfdocument/unlockwithpassword(_:).md)
  Unlocks an encrypted PDF document when a valid password is supplied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/allowsprinting)*