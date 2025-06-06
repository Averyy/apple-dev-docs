# loadMetadata(of:)

**Framework**: Group Activities  
**Kind**: method

Downloads the metadata for the attachment asynchronously and delivers it as the type you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func loadMetadata<MetadataType>(of: MetadataType.Type) async throws -> MetadataType where MetadataType : Decodable, MetadataType : Encodable
```

#### Return Value

The custom metadata object for the attachment.

#### Discussion

Use this function to retrieve any metadata you included with the attachment. You might use this metadata to retrieve app-specific details that aren’t part of the item’s intrinsic data format.

## Parameters

- `of`: The type for your attachment’s custom metadata. This type must   match the one added with the attachment.

## See Also

- [func load<AttachmentType>(AttachmentType.Type) async throws -> AttachmentType](groupsessionjournal/attachment/load(_:).md)
  Downloads the attachment data and asynchronously delivers it as the type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionjournal/attachment/loadmetadata(of:))*