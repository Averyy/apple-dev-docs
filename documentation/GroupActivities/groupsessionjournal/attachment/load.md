# load(_:)

**Framework**: Group Activities  
**Kind**: method

Downloads the attachment data and asynchronously delivers it as the type you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func load<AttachmentType>(_ attachmentType: AttachmentType.Type) async throws -> AttachmentType where AttachmentType : Transferable
```

#### Return Value

A requested type that contains the downloaded information.

#### Discussion

Use this function to retrieve the file or data another participant provides. The method asynchronously retrieves and decodes the data, returning it as the requested type. If the requested type isn’t available, the method throws an error.

## Parameters

- `attachmentType`: The type you use to interpret the data. An app   typically uploads and downloads a single type of data for an activity.   For more information about defining your types, see   .

## See Also

- [func loadMetadata<MetadataType>(of: MetadataType.Type) async throws -> MetadataType](groupsessionjournal/attachment/loadmetadata(of:).md)
  Downloads the metadata for the attachment asynchronously and delivers it as the type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionjournal/attachment/load(_:))*