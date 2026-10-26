# previewWithPassThumbnail:localizedDescription:

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Initializes properties you need to preview an object that represents the pass you add to Wallet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS
- visionOS 2.0+

## Declaration

```objc
+ (instancetype) previewWithPassThumbnail:(CGImageRef) passThumbnail localizedDescription:(NSString *) description;
```

#### Return Value

Returns an object that represents the pass you add to Wallet.

## Parameters

- `passThumbnail`: A CGImage object representing the card artwork for the pass.
- `description`: A localized description for the pass.

## See Also

### Creating a preview of the pass
- [init(passThumbnail: CGImage, localizedDescription: String)](./init%28passthumbnail,localizeddescription%29.md)
  Provides a preview of an image object that represents the pass you add to Wallet.
- [var localizedDescription: String?](./localizeddescription.md)
  A localized description of the pass.
- [var passThumbnailImage: CGImage?](./passthumbnailimage.md)
  A CGImage object representing the card artwork of the pass you use during provisioning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassmetadatapreview/previewwithpassthumbnail:localizeddescription:)*