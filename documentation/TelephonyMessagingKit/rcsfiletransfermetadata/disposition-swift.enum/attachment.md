# RCSFileTransferMetadata.Disposition.attachment

**Framework**: TelephonyMessagingKit  
**Kind**: case

The attachment disposition, directing the receiving app to not automatically render the file.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
case attachment
```

#### Discussion

The code that receives a file with this disposition needs to wait for another action by the person using the app before rendering or otherwise handling the file.

## See Also

- [RCSFileTransferMetadata.Disposition.render](rcsfiletransfermetadata/disposition-swift.enum/render.md)
  The render disposition, directing the receiving app to render the file automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsfiletransfermetadata/disposition-swift.enum/attachment)*