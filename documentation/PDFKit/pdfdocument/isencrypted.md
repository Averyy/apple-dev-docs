# isEncrypted

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value specifying whether the document is encrypted.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isEncrypted: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isEncrypted;
```

## Return Value

[`true`](../../Swift/true.md) if the document is encrypted, whether it is locked or unlocked; [`false`](../../Swift/false.md) otherwise.

## Discussion

If encrypted, reading the document requires a password.

Encrypted documents whose password is the empty string are unlocked automatically upon opening, because PDF Kit tries the empty string as a password if none is supplied. Use the [`unlock(withPassword:)`](./unlock%28withpassword%29.md) method to unlock a document using a password.

## See Also

### Managing Document Security
- [var isLocked: Bool](./islocked.md)
  A Boolean value indicating whether the document is locked.
- [func unlock(withPassword: String) -> Bool](./unlock%28withpassword%29.md)
  Attempts to unlock an encrypted document.
- [var permissionsStatus: PDFDocumentPermissions](./permissionsstatus.md)
  The permissions status of the PDF document.
- [Permission Properties](../permission-properties.md)
  Properties that specify what functions are allowed for a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/isencrypted)*