# init(url:)

**Framework**: UIKit  
**Kind**: init

Creates a document properties object from document data at the URL you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(url: URL)
```

#### Discussion

When you initialize a document properties object with a URL, UIKit automatically finds the corresponding metadata and stores it in the document properties object’s [`metadata`](uidocumentproperties/metadata.md) property.

## Parameters

- `url`: The URL that points to the document data.

## See Also

- [init(metadata: LPLinkMetadata)](uidocumentproperties/init(metadata:).md)
  Creates a document properties object from the metadata object you specify.
- [var metadata: LPLinkMetadata](uidocumentproperties/metadata.md)
  The document’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentproperties/init(url:))*