# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The document browser’s delegate.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIDocumentBrowserViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIDocumentBrowserViewControllerDelegate> delegate;
```

#### Discussion

The delegate object must implement the [`UIDocumentBrowserViewControllerDelegate`](../uidocumentbrowserviewcontrollerdelegate.md) protocol.

## See Also

### Responding to browser events
- [protocol UIDocumentBrowserViewControllerDelegate](../uidocumentbrowserviewcontrollerdelegate.md)
  The protocol you implement to respond as the user interacts with the document browser.
- [func importDocument(at: URL, nextToDocumentAt: URL, mode: UIDocumentBrowserViewController.ImportMode, completionHandler: (URL?, (any Error)?) -> Void)](./importdocument%28at,nexttodocumentat,mode,completionhandler%29.md)
  Imports a document into the same location as an existing document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/delegate)*