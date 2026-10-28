# originalURL

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The URL of the file to be exported. (read-only)

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For more information, see [`UIDocumentPickerExtensionViewController`](../uidocumentpickerextensionviewcontroller.md).

## Declaration

```swift
var originalURL: URL? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSURL * originalURL;
```

## Discussion

While in UIDocumentPickerModeExportToService mode, this property contains the original URL of the file to be copied. Otherwise it is `nil`.

## See Also

### Managing the user interface
- [func dismissGrantingAccess(to: URL?)](./dismissgrantingaccess%28to%29.md)
  Dismisses the document picker.
- [var documentPickerMode: UIDocumentPickerMode](./documentpickermode.md)
  The document picker’s file-transfer operation. (read-only)
- [var documentStorageURL: URL?](./documentstorageurl.md)
  The root URL for documents provided by the corresponding File Provider extension. (read-only)
- [func prepareForPresentation(in: UIDocumentPickerMode)](./prepareforpresentation%28in%29.md)
  Performs any custom configuration of the document picker view controller.
- [var providerIdentifier: String](./provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)
- [var validTypes: [String]?](./validtypes.md)
  An array of valid uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/originalurl)*