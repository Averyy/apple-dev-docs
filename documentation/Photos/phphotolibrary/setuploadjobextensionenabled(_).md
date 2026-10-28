# setUploadJobExtensionEnabled(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Enables or disables the background asset resource upload job feature.

**Availability**:
- iOS 26.1+ - Deprecated in 27.0
- iPadOS 26.1+ - Deprecated in 27.0
- Mac Catalyst 26.1+ - Deprecated in 27.0

> **Deprecated**: Use -enableUploadJobExtensionWithOptions:error: and -disableUploadJobExtensionWithError: instead

## Declaration

```swift
func setUploadJobExtensionEnabled(_ enable: Bool) throws
```

```objc
- (BOOL) setUploadJobExtensionEnabled:(BOOL) enable error:(NSError **) error;
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)

## Discussion

You must call this function before you create [`PHAssetResourceUploadJob`](../phassetresourceuploadjob.md) in the extension’s host application.

To enable background uploads, you must have both full library access and register the extension with the extension point: “com.apple.photos.background-upload”.

## Parameters

- `enable`: `true` allows calls to the extension’s host application; you can fulfill that protocol to create [`PHAssetResourceUploadJob`](../phassetresourceuploadjob.md) objects. `false` stops calls to the extension’s host application.

## See Also

### Enabling an Upload Job Extension
- [var uploadJobExtensionEnabled: Bool](./uploadjobextensionenabled.md)
  A Boolean value that indicates whether background asset resource uploading is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/setuploadjobextensionenabled(_:))*