# uploadJobExtensionEnabled

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether background asset resource uploading is enabled.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var uploadJobExtensionEnabled: Bool { get }
```

```objc
@property (readonly, getter=isUploadJobExtensionEnabled) BOOL uploadJobExtensionEnabled;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## Discussion

The value is `true` if the extension is enabled and active, and is `false` otherwise.

The extension’s host app uses this property to determine the background processing status. See [`PHAssetResourceUploadJob`](../phassetresourceuploadjob.md) and [`PHAssetResourceUploadJobChangeRequest`](../phassetresourceuploadjobchangerequest.md) for more information.

## See Also

### Enabling an Upload Job Extension
- [func setUploadJobExtensionEnabled(Bool) throws](./setuploadjobextensionenabled%28_%29.md)
  Enables or disables the background asset resource upload job feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/uploadjobextensionenabled)*