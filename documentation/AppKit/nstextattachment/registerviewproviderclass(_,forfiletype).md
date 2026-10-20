# registerViewProviderClass(_:forFileType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Registers a specific file type with the attachment view provider.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func registerViewProviderClass(_ textAttachmentViewProviderClass: AnyClass, forFileType fileType: String)
```

```objc
+ (void) registerTextAttachmentViewProviderClass:(Class) textAttachmentViewProviderClass forFileType:(NSString *) fileType;
```

## Parameters

- `textAttachmentViewProviderClass`: The text attachment view provider class.
- `fileType`: A [`String`](../../Swift/string.md) that represents the file type.

## See Also

### Convenience methods
- [class func textAttachmentViewProviderClass(forFileType: String) -> AnyClass?](./textattachmentviewproviderclass%28forfiletype%29.md)
  Returns the text attachment view provider class, if any, for the file type you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/registerviewproviderclass(_:forfiletype:))*