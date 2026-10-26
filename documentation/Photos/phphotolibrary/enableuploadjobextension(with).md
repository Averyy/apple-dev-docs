# enableUploadJobExtension(with:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Enables the background asset resource upload job feature with the given options, atomically.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
func enableUploadJobExtension(with options: PHAssetResourceUploadJobOptions?) throws
```

```objc
- (BOOL) enableUploadJobExtensionWithOptions:(PHAssetResourceUploadJobOptions *) options error:(NSError **) error;
```

#### Discussion

The configuration is created with `options` already set, as a single change — unlike calling [`setUploadJobExtensionOptions(_:)`](./setuploadjobextensionoptions%28_%29.md) afterward, as a separate change.

## Parameters

- `options`: The options to set for the newly enabled configuration, or `nil` to use default values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/enableuploadjobextension(with:))*