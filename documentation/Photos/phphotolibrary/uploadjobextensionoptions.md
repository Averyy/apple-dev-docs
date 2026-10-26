# uploadJobExtensionOptions

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The options for the calling app’s background asset resource upload job configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var uploadJobExtensionOptions: PHAssetResourceUploadJobOptions? { get }
```

```objc
@property (readonly, nullable) PHAssetResourceUploadJobOptions * uploadJobExtensionOptions;
```

#### Discussion

The value is `nil` if the extension isn’t enabled or the caller isn’t authorized. Otherwise, the value is an options object with default values if the configuration exists but no options have been set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/uploadjobextensionoptions)*