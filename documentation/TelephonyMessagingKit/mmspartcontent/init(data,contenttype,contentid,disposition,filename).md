# init(data:contentType:contentID:disposition:fileName:)

**Framework**: TelephonyMessagingKit  
**Kind**: init  
**Role**: Initializer

Creates an MMS part with the provided values.

**Availability**:
- iOS 26.0+

## Declaration

```swift
init(data: Data, contentType: UTType?, contentID: String, disposition: MMSPartContent.MMSDispositionType, fileName: String)
```

## Parameters

- `data`: The raw data of the MMS part.
- `contentType`: The content type of the MMS part, as a [`UTType`](../../UniformTypeIdentifiers/uttype-swift.struct.md).
- `contentID`: The identifier of the MMS part.
- `disposition`: The disposition of the MMS part, indicating whether the part renders inline or as an attachment.
- `fileName`: The file name of the MMS part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmspartcontent/init(data:contenttype:contentid:disposition:filename:))*