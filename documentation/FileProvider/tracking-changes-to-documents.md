# Tracking Changes to Documents

**Framework**: File Provider

Track and report changes to open documents.

#### Overview

The File Provider extension must report any  changes to a document’s content while the user is viewing the document.

![An illustration showing an external update to a document.](/images/com.apple.fileprovider/media-2943054@2x.png)

When an app opens a document managed by your File Provider extension (using either an [`NSFilePresenter`](https://developer.apple.com/documentation/foundation/nsfilepresenter) or [`UIDocument`](https://developer.apple.com/documentation/uikit/uidocument) object), the system requests an enumerator for that document. This enumerator is used only for tracking changes to the document from other processes (for example, updates from another device).

The document enumerator remains active as long as the document is open. Any calls to its [`enumerateChanges(for:from:)`](nsfileproviderenumerator/enumeratechanges(for:from:).md) method should return only information about the specified document.

These changes are forwarded to the [`NSFilePresenter`](https://developer.apple.com/documentation/foundation/nsfilepresenter) or [`UIDocument`](https://developer.apple.com/documentation/uikit/uidocument) that is monitoring the document. The app then updates its user interface as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/tracking-changes-to-documents)*