# init(metadata:)

**Framework**: UIKit  
**Kind**: init

Creates a document properties object from the metadata object you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(metadata: LPLinkMetadata)
```

#### Discussion

If you don’t have a URL backing your document, create a metadata object manually to initialize a document properties object.

## Parameters

- `metadata`: Metadata about a document.

## See Also

- [init(url: URL)](uidocumentproperties/init(url:).md)
  Creates a document properties object from document data at the URL you specify.
- [var metadata: LPLinkMetadata](uidocumentproperties/metadata.md)
  The document’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentproperties/init(metadata:))*