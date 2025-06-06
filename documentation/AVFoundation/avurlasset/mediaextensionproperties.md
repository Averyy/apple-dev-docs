# mediaExtensionProperties

**Framework**: AVFoundation  
**Kind**: property

The properties of the media extension format reader that decodes the asset.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var mediaExtensionProperties: AVMediaExtensionProperties? { get }
```

#### Discussion

If the system decodes the asset using a MediaExtension format reader, the property value contains a valid object that describes the extension. Otherwise, this property value is `nil`.

## See Also

- [class AVMediaExtensionProperties](avmediaextensionproperties.md)
  An object that describes a Media Extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/mediaextensionproperties)*