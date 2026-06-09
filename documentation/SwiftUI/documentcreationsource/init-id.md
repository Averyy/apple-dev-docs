# init(id:)

**Framework**: SwiftUI  
**Kind**: init

Creates a document creation source with the given identifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(id: String)
```

#### Discussion

Use different sources to distinguish between document creation flows in your app.

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

When a document is created, you can retrieve its source from [`URLDocumentConfiguration`](urldocumentconfiguration.md) or [`FileDocumentConfiguration`](filedocumentconfiguration.md).

## Parameters

- `id`: A string that uniquely identifies the creation flow within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentcreationsource/init(id:))*