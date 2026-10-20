# textAttachmentViewProviderClass(forFileType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the text attachment view provider class, if any, for the file type you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func textAttachmentViewProviderClass(forFileType fileType: String) -> AnyClass?
```

```objc
+ (Class) textAttachmentViewProviderClassForFileType:(NSString *) fileType;
```

#### Return Value

The text attachment view provider class, or `nil` if the there is no class for the specified file type.

## Parameters

- `fileType`: A [`String`](../../Swift/string.md) that represents the file type.

## See Also

### Convenience methods
- [class func registerViewProviderClass(AnyClass, forFileType: String)](./registerviewproviderclass%28_,forfiletype%29.md)
  Registers a specific file type with the attachment view provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachment/textattachmentviewproviderclass(forfiletype:))*