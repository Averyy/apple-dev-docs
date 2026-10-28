# dismissGrantingAccess(to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the document picker.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For more information, see [`UIDocumentPickerExtensionViewController`](../uidocumentpickerextensionviewcontroller.md).

## Declaration

```swift
func dismissGrantingAccess(to url: URL?)
```

```objc
- (void) dismissGrantingAccessToURL:(NSURL *) url;
```

## Discussion

Call this method when the user selects a document or destination. This method dismisses the document picker view controller in the host app and triggers the appropriate file transfer. After the transfer is complete, the method passes the provided URL to the host app’s [`documentPicker(_:didPickDocumentAt:)`](../uidocumentpickerdelegate/documentpicker%28_,didpickdocumentat%29.md) delegate method.

The URL must meet all of the following conditions:

- Import Document Picker mode. Provide a URL for the selected file. The URL only needs to be accessible by the Document Picker View Controller extension.
- Open Document Picker mode. Provide a URL for the selected file. The URL must point to a location inside the directory hierarchy referred to by your [`documentStorageURL`](./documentstorageurl.md) property.
- Export Document Picker mode. Before calling this method, copy the file to the selected destination. Your extensions also need to track the file and make sure it is synced to your server.

After the copy is complete, call this method and provide the URL to the new copy.  This URL needs to be accessible only by the Document Picker View Controller extension. The system returns the URL to the host app to indicate success; however, the host app cannot access the document at this URL.

- Move Document Picker mode. Before calling this method, copy the file to the selected destination. Your extensions also need to track the file and make sure it is synced to your server.

After the copy is complete, call this method and provide the URL to the new copy. The URL needs to be contained inside the hierarchy referred to by your [`documentStorageURL`](./documentstorageurl.md) property. The system returns this URL to the host app, and the host app can continue to access the document at this URL.

## Parameters

- `url`: The URL that the extension returns to the host app.

## See Also

### Managing the user interface
- [var documentPickerMode: UIDocumentPickerMode](./documentpickermode.md)
  The document picker’s file-transfer operation. (read-only)
- [var documentStorageURL: URL?](./documentstorageurl.md)
  The root URL for documents provided by the corresponding File Provider extension. (read-only)
- [var originalURL: URL?](./originalurl.md)
  The URL of the file to be exported. (read-only)
- [func prepareForPresentation(in: UIDocumentPickerMode)](./prepareforpresentation%28in%29.md)
  Performs any custom configuration of the document picker view controller.
- [var providerIdentifier: String](./provideridentifier.md)
  An identifier shared by this Document Picker extension and its corresponding File Provider extension. (read-only)
- [var validTypes: [String]?](./validtypes.md)
  An array of valid uniform type identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerextensionviewcontroller/dismissgrantingaccess(to:))*