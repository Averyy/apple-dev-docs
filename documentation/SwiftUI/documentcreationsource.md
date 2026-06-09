# DocumentCreationSource

**Framework**: SwiftUI  
**Kind**: struct

Describes the source used to create a new document.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DocumentCreationSource
```

#### Overview

On iOS, you can declare custom creation sources and use them in [`NewDocumentButton`](newdocumentbutton.md).

```swift
extension DocumentCreationSource {
    static let scanner: Self =
        DocumentCreationSource(id: "document-from-scanner")

    static let template: Self =
        DocumentCreationSource(id: "document-from-template")
}

DocumentGroupLaunchScene("Documents") {
    NewDocumentButton("Scan Document", source: .scanner)
    NewDocumentButton("New from Template", source: .template)
}
```

When a document is created, you can retrieve its source from [`URLDocumentConfiguration`](urldocumentconfiguration.md) or [`FileDocumentConfiguration`](filedocumentconfiguration.md):

```swift
DocumentGroup(newDocument: { MyDocument() }) { configuration in
    if configuration.creationSource == .template {
        TemplateSetupView()
    }
}
```

## Topics

### Creating a source
- [init(id: String)](documentcreationsource/init(id:).md)
  Creates a document creation source with the given identifier.
### Identifying a source
- [let id: String](documentcreationsource/id.md)
  A string that uniquely identifies this creation source within your app.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DocumentGroupLaunchScene](documentgrouplaunchscene.md)
  A launch scene for document-based applications.
- [struct DocumentLaunchView](documentlaunchview.md)
  A view to present when launching document-related user experience.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](view/documentbrowsercontextmenu(_:).md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
- [struct DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md)
  A proxy for access to the frame of the scene and its title view.
- [struct DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md)
  The default actions for the document group launch scene and the document launch view.
- [struct NewDocumentButton](newdocumentbutton.md)
  A button that creates and opens new documents.
- [struct NewDocumentButtonDataSource](newdocumentbuttondatasource.md)
  Describes the source of data used to create a new document.
- [struct DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md)
  The default label used for a new document button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentcreationsource)*