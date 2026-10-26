# localizedDescription

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A localized description of the pass.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS
- visionOS 2.0+

## Declaration

```swift
var localizedDescription: String? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSString * localizedDescription;
```

## See Also

### Creating a preview of the pass
- [init(passThumbnail: CGImage, localizedDescription: String)](./init%28passthumbnail,localizeddescription%29.md)
  Provides a preview of an image object that represents the pass you add to Wallet.
- [var passThumbnailImage: CGImage?](./passthumbnailimage.md)
  A CGImage object representing the card artwork of the pass you use during provisioning.
- [+ previewWithPassThumbnail:localizedDescription:](./previewwithpassthumbnail_localizeddescription_.md)
  Initializes properties you need to preview an object that represents the pass you add to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassmetadatapreview/localizeddescription)*