# unlock(withPassword:)

**Framework**: PDFKit  
**Kind**: method  
**Role**: Instance Method

Attempts to unlock an encrypted document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func unlock(withPassword password: String) -> Bool
```

```objc
- (BOOL) unlockWithPassword:(NSString *) password;
```

#### Return Value

[`true`](../../Swift/true.md) if the specified password unlocks the document, [`false`](../../Swift/false.md) otherwise.

#### Discussion

If the password is correct, this method returns [`true`](../../Swift/true.md), and a `PDFDocumentDidUnlockNotification` notification is sent. Once unlocked, you cannot use this function to relock the document.

If you attempt to unlock an already unlocked document, one of the following occurs:

- If the document is unlocked with full owner permissions, `unlockWithPassword` does nothing and returns [`true`](../../Swift/true.md). The password string is ignored.
- If the document is unlocked with only user permissions, `unlockWithPassword` attempts to obtain full owner permissions with the password string. If the string fails, the document maintains its user permissions. In either case, this method returns [`true`](../../Swift/true.md).

## Parameters

- `password`: The password to unlock an encrypted document (you cannot lock an unlocked PDF document by using an incorrect password).

## See Also

### Managing Document Security
- [var isEncrypted: Bool](./isencrypted.md)
  A Boolean value specifying whether the document is encrypted.
- [var isLocked: Bool](./islocked.md)
  A Boolean value indicating whether the document is locked.
- [var permissionsStatus: PDFDocumentPermissions](./permissionsstatus.md)
  The permissions status of the PDF document.
- [Permission Properties](../permission-properties.md)
  Properties that specify what functions are allowed for a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/unlock(withpassword:))*