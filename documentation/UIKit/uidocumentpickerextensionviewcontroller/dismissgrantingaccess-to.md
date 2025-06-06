# dismissGrantingAccess(to:)

**Framework**: UIKit  
**Kind**: method

Dismisses the document picker.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dismissGrantingAccess(to url: URL?)
```

#### Discussion

Call this method when the user selects a document or destination. This method dismisses the document picker view controller in the host app and triggers the appropriate file transfer. After the transfer is complete, the method passes the provided URL to the host app’s [`documentPicker(_:didPickDocumentAt:)`](uidocumentpickerdelegate/documentpicker(_:didpickdocumentat:).md) delegate method.

The URL must meet all of the following conditions:

- Import Document Picker mode. Provide a URL for the selected file. The URL only needs to be accessible by the Document Picker View Controller extension.
- Open Document Picker mode. Provide a URL for the selected file. The URL must point to a location inside the directory hierarchy referred to by your [`documentStorageURL`](uidocumentpickerextensionviewcontroller/documentstorageurl.md) property.
- Export Document Picker mode. Before calling this method, copy the file to the selected destination. Your extensions also need to track the file and make sure it is synced to your server.

After the copy is complete, call this method and provide the URL to the new copy.  This URL needs to be accessible only by the Document Picker View Controller extension. The system returns the URL to the host app to indicate success; however, the host app cannot access the document at this URL.

- Move Document Picker mode. Before calling this method, copy the file to the selected destination. Your extensions also need to track the file and make sure it is synced to your server.

After the copy is complete, call this method and provide the URL to the new copy. The URL needs to be contained inside the hierarchy referred to by your [`documentStorageURL`](uidocumentpickerextensionviewcontroller/documentstorageurl.md) property. The system returns this URL to the host app, and the host app can continue to access the document at this URL.

## Parameters

- `url`: The URL that the extension returns to the host app.

## See Also

- [var documentPickerMode: UIDocumentPickerMode](uidocumentpickerextensionviewcontroller/documentpickermode.md)
  The document picker’s file-transfer operation. (read-only)
- [var documentStorageURL: URL?](uidocumentpickerextensionviewcontroller/documentstorageurl.md)
  The root URL for documents provided by the corresponding File Provider extension. (read-only)
- [var originalURL: URL?](uidocumentpickerextensionviewcontroller/originalurl.md)
  The URL of the file to be exported. (read-only)
- [func prepareForPresentation(in: UIDocumentPickerMode)](uidocumentpickerextensionviewcontroller/prepareforpresentation(in:).md)
  Performs any custom configuration of the document picker view controller.
- [var providerIdentifier: String](uidocumentpickerextensionviewcontroller/provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)
- [var validTypes: [String]?](uidocumentpickerextensionviewcontroller/validtypes.md)
  An array of valid uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to:))*