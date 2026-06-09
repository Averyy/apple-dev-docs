# init(for:source:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button that creates new documents using data from pasteboard.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
init<D>(for type: D.Type, source: NewDocumentButtonDataSource) where D : FileDocument
```

#### Discussion

```swift
struct NewTextDocumentFromPasteboardButton: View {
    var body: some View {
        NewDocumentButton(
            for: TextDocument.self, source: .pasteboard
        )
    }
}

struct TextDocument: FileDocument { ... }
```

## Parameters

- `type`: Type of documents to create from pasteboard data.
- `source`: A source of data that fills the newly created document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/newdocumentbutton/init(for:source:))*