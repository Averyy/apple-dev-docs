# URLDocumentConfiguration

**Framework**: SwiftUI  
**Kind**: class

The configuration of an open document that stores its file URL, last modification date, and related metadata.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final class URLDocumentConfiguration
```

#### Overview

SwiftUI passes a `URLDocumentConfiguration` to the `makeDocument` closure of [`DocumentGroup`](documentgroup.md). This class is `@Observable` — views and other observers can track changes to [`fileURL`](urldocumentconfiguration/fileurl.md) and other properties.

Use [`makeFileCoordinator()`](urldocumentconfiguration/makefilecoordinator().md) to perform coordinated reads or writes outside the normal [`DocumentReader`](documentreader.md)/[`DocumentWriter`](documentwriter.md) flow — for example, to read a single sub-file of a package document on demand:

```swift
let coordinator = configuration.makeFileCoordinator()
var error: NSError?
coordinator.coordinate(
    readingItemAt: pageURL, options: [], error: &error
) { url in
    let data = try? Data(contentsOf: url)
    // ...
}
```

> ❗ **Important**: Inside [`read(from:progress:)`](documentreader/read(from:progress:).md) and `DocumentWriter/write(content:to:previous:progress:)`, use the `source` / `destination` URL parameter — not [`fileURL`](urldocumentconfiguration/fileurl.md). The configuration’s URL reflects current state and may differ from the operation’s URL after a Save As or rename.

## Topics

### Accessing document properties
- [var fileURL: URL?](urldocumentconfiguration/fileurl.md)
  A URL of the open document if it is saved to disk.
- [var lastContentModificationDate: Date?](urldocumentconfiguration/lastcontentmodificationdate.md)
  The date on which the contents of the document were last modified, if available.
- [var creationSource: DocumentCreationSource?](urldocumentconfiguration/creationsource.md)
  The source associated with the button that created this document.
### Coordinating file access
- [func makeFileCoordinator() -> sending NSFileCoordinator](urldocumentconfiguration/makefilecoordinator.md)
  Creates a file coordinator for coordinated disk access outside the normal read/write flow.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol Document](document.md)
  A document that supports both reading and writing.
- [protocol ReadableDocument](readabledocument.md)
  A document type that supports reading from file.
- [protocol WritableDocument](writabledocument.md)
  A document type that supports writing to file.
- [struct DocumentCreationContext](documentcreationcontext.md)
  Context about how a document was created.
- [protocol DocumentBaseBox](documentbasebox.md)
  A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/urldocumentconfiguration)*