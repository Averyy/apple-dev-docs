# init(documentTypes:in:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a document picker that can open or copy the specified file types.

**Availability**:
- iOS 8.0+ - Deprecated in 14.0
- iPadOS 8.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(forOpeningContentTypes:)`](./init%28foropeningcontenttypes%29.md) or [`init(forOpeningContentTypes:asCopy:)`](./init%28foropeningcontenttypes,ascopy%29.md) instead.

## Declaration

```swift
init(documentTypes allowedUTIs: [String], in mode: UIDocumentPickerMode)
```

```objc
- (instancetype) initWithDocumentTypes:(NSArray<NSString *> *) allowedUTIs inMode:(UIDocumentPickerMode) mode;
```

## Return Value

Returns an initialized `UIDocumentPickerViewController` object, or `nil` if the object could not be successfully initialized.

## Discussion

In iOS 10 and earlier, this method returns the document picker view controller from the most recently used Document Provider extension. If no valid Document Provider can be found, it defaults back to iCloud Drive.

In iOS 11 and later, it returns the standard browser interface. This interface is the same one used by the [`UIDocumentBrowserViewController`](../uidocumentbrowserviewcontroller.md) class.

## Parameters

- `allowedUTIs`: An array of uniform type identifiers (UTIs). UTIs are strings that uniquely identify a file’s type. For more information, see [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).
- `mode`: The type of file-transfer operation that the document picker performs. This argument accepts only the [`UIDocumentPickerMode.import`](../uidocumentpickermode/import.md) or [`UIDocumentPickerMode.open`](../uidocumentpickermode/open.md) mode.

## See Also

### Deprecated methods
- [init(url: URL, in: UIDocumentPickerMode)](./init%28url,in%29.md)
  Initializes and returns a document picker that can export or copy the specified document.
- [init(urls: [URL], in: UIDocumentPickerMode)](./init%28urls,in%29.md)
  Creates and returns a document picker that can export or move the specified documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller/init(documenttypes:in:))*