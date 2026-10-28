# setUploadJobExtensionOptions(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Sets the options for the calling app’s background asset resource upload job configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
func setUploadJobExtensionOptions(_ options: PHAssetResourceUploadJobOptions) throws
```

```objc
- (BOOL) setUploadJobExtensionOptions:(PHAssetResourceUploadJobOptions *) options error:(NSError **) error;
```

## Discussion

To reset the configuration’s options to their default values, pass a newly-initialized `PHAssetResourceUploadJobOptions` instance.

## Parameters

- `options`: The options to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/setuploadjobextensionoptions(_:))*