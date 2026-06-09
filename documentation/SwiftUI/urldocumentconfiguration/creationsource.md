# creationSource

**Framework**: SwiftUI  
**Kind**: property

The source associated with the button that created this document.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final var creationSource: DocumentCreationSource? { get }
```

#### Discussion

On iOS, you can specify the source via a [`NewDocumentButton`](newdocumentbutton.md) in [`DocumentGroupLaunchScene`](documentgrouplaunchscene.md):

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

Use this property to determine which [`NewDocumentButton`](newdocumentbutton.md) triggered the creation of the current document, allowing you to customize the UI accordingly.

## See Also

- [var fileURL: URL?](urldocumentconfiguration/fileurl.md)
  A URL of the open document if it is saved to disk.
- [var lastContentModificationDate: Date?](urldocumentconfiguration/lastcontentmodificationdate.md)
  The date on which the contents of the document were last modified, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/urldocumentconfiguration/creationsource)*