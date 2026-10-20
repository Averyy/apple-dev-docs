# UIDocumentBrowserViewController.ImportMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The document browser’s import modes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum ImportMode
```

```c
enum UIDocumentBrowserImportMode : NSUInteger;
```

## Mentions

- [Customizing a document-based app’s launch experience](../customizing-a-document-based-app-s-launch-experience.md)

## Topics

### Constants
- [UIDocumentBrowserViewController.ImportMode.copy](./importmode/copy.md)
  A mode indicating that the file should be copied into its new location (the original file is left unchanged).
- [UIDocumentBrowserViewController.ImportMode.move](./importmode/move.md)
  A mode indicating that the file should be moved to its new location (the original file should be deleted).
- [UIDocumentBrowserViewController.ImportMode.none](./importmode/none.md)
  A mode indicating that the document can’t be imported.
### Initializers
- [init?(rawValue: UInt)](./importmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating new documents
- [func documentBrowser(UIDocumentBrowserViewController, didRequestDocumentCreationWithHandler: (URL?, UIDocumentBrowserViewController.ImportMode) -> Void)](../uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_,didrequestdocumentcreationwithhandler%29.md)
  Asks the delegate to create a new document.
- [func documentBrowser(UIDocumentBrowserViewController, didImportDocumentAt: URL, toDestinationURL: URL)](../uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_,didimportdocumentat,todestinationurl%29.md)
  Tells the delegate that a document has been successfully imported.
- [func documentBrowser(UIDocumentBrowserViewController, failedToImportDocumentAt: URL, error: (any Error)?)](../uidocumentbrowserviewcontrollerdelegate/documentbrowser%28_,failedtoimportdocumentat,error%29.md)
  Tells the delegate that the document browser failed to import the specified document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/importmode)*