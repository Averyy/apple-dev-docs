# init(metadata:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a document properties object from the metadata object you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
init(metadata: LPLinkMetadata)
```

```objc
- (instancetype) initWithMetadata:(LPLinkMetadata *) metadata;
```

#### Discussion

If you don’t have a URL backing your document, create a metadata object manually to initialize a document properties object.

## Parameters

- `metadata`: Metadata about a document.

## See Also

### Creating a document header
- [init(url: URL)](./init%28url%29-zeio.md)
  Creates a document properties object from document data at the URL you specify.
- [var metadata: LPLinkMetadata](./metadata.md)
  The document’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentproperties/init(metadata:))*