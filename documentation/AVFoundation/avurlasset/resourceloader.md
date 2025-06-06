# resourceLoader

**Framework**: AVFoundation  
**Kind**: property

The resource loader for the asset.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var resourceLoader: AVAssetResourceLoader { get }
```

#### Discussion

During loading, the system may ask the resource loader to assist loading the resource. For example, a resource that requires decryption may require the resource loader to provide the appropriate decryption keys. You can assign a delegate object to the resource loader object and use your delegate to intercept these requests and provide appropriate responses.

## See Also

- [var mayRequireContentKeysForMediaDataProcessing: Bool](avurlasset/mayrequirecontentkeysformediadataprocessing.md)
  A Boolean value that indicates whether you can add this asset as a content key recipient to a content key session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/resourceloader)*