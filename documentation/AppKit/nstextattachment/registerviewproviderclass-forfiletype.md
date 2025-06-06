# registerViewProviderClass(_:forFileType:)

**Framework**: AppKit  
**Kind**: method

Registers a specific file type with the attachment view provider.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func registerViewProviderClass(_ textAttachmentViewProviderClass: AnyClass, forFileType fileType: String)
```

## Parameters

- `textAttachmentViewProviderClass`: The text attachment view provider class.
- `fileType`: A   that represents the file type.

## See Also

- [class func textAttachmentViewProviderClass(forFileType: String) -> AnyClass?](nstextattachment/textattachmentviewproviderclass(forfiletype:).md)
  Returns the text attachment view provider class, if any, for the file type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/registerviewproviderclass(_:forfiletype:))*