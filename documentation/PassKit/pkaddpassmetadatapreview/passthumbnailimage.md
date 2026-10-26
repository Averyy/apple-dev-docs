# passThumbnailImage

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A CGImage object representing the card artwork of the pass you use during provisioning.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS
- visionOS 2.0+

## Declaration

```swift
unowned(unsafe) var passThumbnailImage: CGImage? { get }
```

```objc
@property (nonatomic, assign, readonly, nullable) CGImageRef passThumbnailImage;
```

## See Also

### Creating a preview of the pass
- [init(passThumbnail: CGImage, localizedDescription: String)](./init%28passthumbnail,localizeddescription%29.md)
  Provides a preview of an image object that represents the pass you add to Wallet.
- [var localizedDescription: String?](./localizeddescription.md)
  A localized description of the pass.
- [+ previewWithPassThumbnail:localizedDescription:](./previewwithpassthumbnail_localizeddescription_.md)
  Initializes properties you need to preview an object that represents the pass you add to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassmetadatapreview/passthumbnailimage)*