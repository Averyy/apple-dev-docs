# init(artworkID:previewImageRequestHandler:videoAssetFileURLRequestHandler:)

**Framework**: Media Player  
**Kind**: init

Creates an animated artwork.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
convenience init(artworkID: String, previewImageRequestHandler: @escaping (CGSize) async -> UIImage?, videoAssetFileURLRequestHandler: @escaping (CGSize) async -> URL?)
```

## Parameters

- `artworkID`: A unique identifier for this animated artwork. This identifier should   encapsulate the identity of both the preview frame and video asset. If you change either,   you should provide an   with an updated  .
- `previewImageRequestHandler`: A handler to return a preview image for this artwork, for   the requested   in pixels. You can return   if the preview image cannot be   resolved for any reason. The   you return should ideally have a size equal to the   requested  , however an image of the same aspect ratio is acceptable. Images that   diverge significantly from the requested aspect ratio may be rejected by the system. Aim   to return preview images quickly and ideally synchronously, and if possible you should   preload these images in order to reduce perceived latency when displaying animated artwork   to the user.
- `videoAssetFileURLRequestHandler`: A handler to return a file   for the artwork video   asset for this artwork, for the requested   in pixels. You can return   if the   artwork video asset cannot be resolved for any reason. The   you return must reference   a local asset, ideally with a size equal to the requested  , however an asset with   the same aspect ratio is acceptable. Assets that diverge significantly from the requested   aspect ratio may be rejected by the system. The video assets you provide should loop   cleanly, and should be available relatively quickly from this handler (particularly when   re-fetched). It’s advised that assets are cached for subsequent fetches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemanimatedartwork/init(artworkid:previewimagerequesthandler:videoassetfileurlrequesthandler:)-7bb3j)*