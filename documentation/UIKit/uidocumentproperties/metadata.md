# metadata

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The document’s metadata.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var metadata: LPLinkMetadata { get set }
```

```objc
@property (nonatomic, copy, readwrite) LPLinkMetadata * metadata;
```

#### Discussion

If you initialize the document properties object using [`init(url:)`](./init%28url%29-zeio.md), UIKit generates this metadata automatically. Typically, you don’t need to access the value of this property directly because UIKit updates the metadata asynchronously to display the latest information in the document header.

If you initialize the document properties object using [`init(metadata:)`](./init%28metadata%29.md), you can use this property to manually set metadata if it requires an update.

## See Also

### Creating a document header
- [init(url: URL)](./init%28url%29-zeio.md)
  Creates a document properties object from document data at the URL you specify.
- [init(metadata: LPLinkMetadata)](./init%28metadata%29.md)
  Creates a document properties object from the metadata object you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentproperties/metadata)*