# init(documentTypes:in:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a document picker that can open or copy the specified file types.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(documentTypes allowedUTIs: [String], in mode: UIDocumentPickerMode)
```

#### Return Value

Returns an initialized `UIDocumentPickerViewController` object, or `nil` if the object could not be successfully initialized.

#### Discussion

In iOS 10 and earlier, this method returns the document picker view controller from the most recently used Document Provider extension. If no valid Document Provider can be found, it defaults back to iCloud Drive.

In iOS 11 and later, it returns the standard browser interface. This interface is the same one used by the [`UIDocumentBrowserViewController`](uidocumentbrowserviewcontroller.md) class.

## Parameters

- `allowedUTIs`: An array of uniform type identifiers (UTIs). UTIs are strings that uniquely identify a file’s type. For more information, see  .
- `mode`: The type of file-transfer operation that the document picker performs. This argument accepts only the   or   mode.

## See Also

- [init(url: URL, in: UIDocumentPickerMode)](uidocumentpickerviewcontroller/init(url:in:).md)
  Initializes and returns a document picker that can export or copy the specified document.
- [init(urls: [URL], in: UIDocumentPickerMode)](uidocumentpickerviewcontroller/init(urls:in:).md)
  Creates and returns a document picker that can export or move the specified documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(documenttypes:in:))*