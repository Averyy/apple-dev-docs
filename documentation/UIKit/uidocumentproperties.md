# UIDocumentProperties

**Framework**: Uikit  
**Kind**: class

Information that UIKit uses to generate a document header for a navigation item’s title menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDocumentProperties
```

#### Overview

Assign a [`UIDocumentProperties`](uidocumentproperties.md) object to your navigation item’s [`documentProperties`](uinavigationitem/documentproperties.md) property. UIKit uses this object to display a document header at the top of the title menu, which appears when a person taps the navigation item’s title. The document header displays information about the current document, such as its title, file type, and size.

![Title menu with a document header that contains a document preview, a Share button, and the text New Document, Text Document, 1 byte.](https://docs-assets.developer.apple.com/published/0811f4d9adcb9fcb3625d31fb223b7d1/media-3975665%402x.png)

Additionally, you can configure a set of sharing capabilities that allow people to share or drag and drop the document content from the document header:

- Set an [`activityViewControllerProvider`](uidocumentproperties/activityviewcontrollerprovider.md) to show the Share button.
- Set a [`dragItemsProvider`](uidocumentproperties/dragitemsprovider.md) to allow people to drag and drop the document by dragging the preview icon.

> **Note**:  Session 10069: [`Meet desktop-class iPad`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10069) Session 10070: [`Build a desktop-class iPad app`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10070)

## Topics

### Creating a document header
- [init(url: URL)](uidocumentproperties/init(url:).md)
  Creates a document properties object from document data at the URL you specify.
- [init(metadata: LPLinkMetadata)](uidocumentproperties/init(metadata:).md)
  Creates a document properties object from the metadata object you specify.
- [var metadata: LPLinkMetadata](uidocumentproperties/metadata.md)
  The document’s metadata.
### Generating a document preview
- [var wantsIconRepresentation: Bool](uidocumentproperties/wantsiconrepresentation.md)
  A Boolean value that determines whether to render an icon of the document in the navigation bar.
### Supporting drag and drop
- [var dragItemsProvider: ((any UIDragSession) -> [UIDragItem])?](uidocumentproperties/dragitemsprovider.md)
  A closure that provides drag items that represent the document.
### Supporting sharing
- [var activityViewControllerProvider: (() -> UIActivityViewController)?](uidocumentproperties/activityviewcontrollerprovider.md)
  A closure that provides an activity view controller for sharing the document.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var titleMenuProvider: (([UIMenuElement]) -> UIMenu?)?](uinavigationitem/titlemenuprovider.md)
  A closure that generates the navigation item’s title menu.
- [var documentProperties: UIDocumentProperties?](uinavigationitem/documentproperties.md)
  An object that provides the document header for the title menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentproperties)*