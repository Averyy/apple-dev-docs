# sidecarURL

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The sidecar URL used by the MediaExtension.

**Availability**:
- macOS 26.0+

## Declaration

```objc
@property (nonatomic, readonly, nullable) NSURL * sidecarURL;
```

#### Discussion

The sidecar URL is returned only if the MediaExtension format reader supports sidecar files, and implements this property [MEFileInfo setSidecarFilename:]. Will return nil otherwise.

## See Also

### Accessing Media Extension properties
- [var mediaExtensionProperties: AVMediaExtensionProperties?](./mediaextensionproperties.md)
  The properties of the media extension format reader that decodes the asset.
- [class AVMediaExtensionProperties](../avmediaextensionproperties.md)
  An object that describes a Media Extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/sidecarurl)*