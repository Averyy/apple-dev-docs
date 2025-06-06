# passThumbnailImage

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A CGImage object representing the card artwork of the pass you use during provisioning.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
unowned(unsafe) var passThumbnailImage: CGImage? { get }
```

## See Also

- [init(passThumbnail: CGImage, localizedDescription: String)](pkaddpassmetadatapreview/init(passthumbnail:localizeddescription:).md)
  Provides a preview of an image object that represents the pass you add to Wallet.
- [var localizedDescription: String?](pkaddpassmetadatapreview/localizeddescription.md)
  A localized description of the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassmetadatapreview/passthumbnailimage)*