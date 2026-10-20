# permissionsStatus

**Framework**: PDFKit  
**Kind**: property  
**Role**: Instance Property

The permissions status of the PDF document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var permissionsStatus: PDFDocumentPermissions { get }
```

```objc
@property (nonatomic, readonly) PDFDocumentPermissions permissionsStatus;
```

## See Also

### Managing Document Security
- [var isEncrypted: Bool](./isencrypted.md)
  A Boolean value specifying whether the document is encrypted.
- [var isLocked: Bool](./islocked.md)
  A Boolean value indicating whether the document is locked.
- [func unlock(withPassword: String) -> Bool](./unlock%28withpassword%29.md)
  Attempts to unlock an encrypted document.
- [Permission Properties](../permission-properties.md)
  Properties that specify what functions are allowed for a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfdocument/permissionsstatus)*