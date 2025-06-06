# init(url:in:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a document picker that can export or copy the specified document.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(url: URL, in mode: UIDocumentPickerMode)
```

#### Return Value

Returns an initialized `UIDocumentPickerViewController` object, or `nil` if the object could not be successfully initialized.

#### Discussion

In iOS 10 and earlier, this method returns the document picker view controller from the most recently used Document Provider extension. If no valid Document Provider can be found, it defaults back to iCloud Drive.

In iOS 11 and later, it returns the standard browser interface. This interface is the same one used by the [`UIDocumentBrowserViewController`](uidocumentbrowserviewcontroller.md) class.

## Parameters

- `url`: The document that the document picker exports or moves.
- `mode`: The type of file-transfer operation that the document picker performs. This argument accepts only the   or   mode.

## See Also

- [init(documentTypes: [String], in: UIDocumentPickerMode)](uidocumentpickerviewcontroller/init(documenttypes:in:).md)
  Creates and returns a document picker that can open or copy the specified file types.
- [init(urls: [URL], in: UIDocumentPickerMode)](uidocumentpickerviewcontroller/init(urls:in:).md)
  Creates and returns a document picker that can export or move the specified documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(url:in:))*