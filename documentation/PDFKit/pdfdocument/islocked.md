# isLocked

**Framework**: PDFKit  
**Kind**: property

A Boolean value indicating whether the document is locked.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isLocked: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the document is locked; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

Only encrypted documents can be locked. Encrypted documents whose password is the empty string are unlocked automatically upon opening, because PDF Kit tries the empty string as a password if none is supplied. Use the [`unlock(withPassword:)`](pdfdocument/unlock(withpassword:).md) method to unlock a document using a password.

## See Also

- [var isEncrypted: Bool](pdfdocument/isencrypted.md)
  A Boolean value specifying whether the document is encrypted.
- [func unlock(withPassword: String) -> Bool](pdfdocument/unlock(withpassword:).md)
  Attempts to unlock an encrypted document.
- [var permissionsStatus: PDFDocumentPermissions](pdfdocument/permissionsstatus.md)
  The permissions status of the PDF document.
- [Permission Properties](permission-properties.md)
  Properties that specify what functions are allowed for a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/islocked)*