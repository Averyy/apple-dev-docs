# metadata

**Framework**: UIKit  
**Kind**: property

The document’s metadata.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var metadata: LPLinkMetadata { get set }
```

#### Discussion

If you initialize the document properties object using [`init(url:)`](uidocumentproperties/init(url:).md), UIKit generates this metadata automatically. Typically, you don’t need to access the value of this property directly because UIKit updates the metadata asynchronously to display the latest information in the document header.

If you initialize the document properties object using [`init(metadata:)`](uidocumentproperties/init(metadata:).md), you can use this property to manually set metadata if it requires an update.

## See Also

- [init(url: URL)](uidocumentproperties/init(url:).md)
  Creates a document properties object from document data at the URL you specify.
- [init(metadata: LPLinkMetadata)](uidocumentproperties/init(metadata:).md)
  Creates a document properties object from the metadata object you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentproperties/metadata)*