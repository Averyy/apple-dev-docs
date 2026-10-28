# init(passThumbnail:localizedDescription:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Provides a preview of an image object that represents the pass you add to Wallet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS
- visionOS 2.0+

## Declaration

```swift
init(passThumbnail: CGImage, localizedDescription description: String)
```

```objc
- (instancetype) initWithPassThumbnail:(CGImageRef) passThumbnail localizedDescription:(NSString *) description;
```

## Discussion

This method throws an `invalidInput` error if a JPKI applet doesn’t back the pass.

## Parameters

- `passThumbnail`: A CGImage object that represents the card artwork of the pass you use during provisioning.
- `description`: A localized description of the pass.

## See Also

### Creating a preview of the pass
- [var localizedDescription: String?](./localizeddescription.md)
  A localized description of the pass.
- [var passThumbnailImage: CGImage?](./passthumbnailimage.md)
  A CGImage object representing the card artwork of the pass you use during provisioning.
- [+ previewWithPassThumbnail:localizedDescription:](./previewwithpassthumbnail_localizeddescription_.md)
  Initializes properties you need to preview an object that represents the pass you add to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassmetadatapreview/init(passthumbnail:localizeddescription:))*