# init(urls:in:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a document picker that can export or move the specified documents.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(forExporting:)`](./init%28forexporting%29.md) or [`init(forExporting:asCopy:)`](./init%28forexporting,ascopy%29.md) instead.

## Declaration

```swift
init(urls: [URL], in mode: UIDocumentPickerMode)
```

```objc
- (instancetype) initWithURLs:(NSArray<NSURL *> *) urls inMode:(UIDocumentPickerMode) mode;
```

#### Return Value

Returns an initialized `UIDocumentPickerViewController` object, or `nil` if the object could not be successfully initialized.

#### Discussion

In iOS 10 and earlier, this method returns the document picker view controller from the most recently used Document Provider extension. If no valid Document Provider can be found, it defaults back to iCloud Drive.

In iOS 11 and later, it returns the standard browser interface. This interface is the same one used by the [`UIDocumentBrowserViewController`](../uidocumentbrowserviewcontroller.md) class.

## Parameters

- `urls`: An array of documents that the document picked exports or moves.
- `mode`: The type of file-transfer operation that the document picker performs. This argument accepts only the [`UIDocumentPickerMode.exportToService`](../uidocumentpickermode/exporttoservice.md) or [`UIDocumentPickerMode.moveToService`](../uidocumentpickermode/movetoservice.md) mode.

## See Also

### Deprecated methods
- [init(documentTypes: [String], in: UIDocumentPickerMode)](./init%28documenttypes,in%29.md)
  Creates and returns a document picker that can open or copy the specified file types.
- [init(url: URL, in: UIDocumentPickerMode)](./init%28url,in%29.md)
  Initializes and returns a document picker that can export or copy the specified document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(urls:in:))*