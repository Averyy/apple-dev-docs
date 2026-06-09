# minimumTileExtendRect(forTileRect:sourceRGBASize:)

**Framework**: Cinematic  
**Kind**: method

Returns the minimum source rect that must be sampled to render tileRect without edge artifacts.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
class func minimumTileExtendRect(forTileRect tileRect: CGRect, sourceRGBASize: CGSize) -> CGRect
```

#### Return Value

A rect (in full-image pixel coordinates) covering the minimum required source region, clamped to the image bounds.

#### Discussion

When applying a bokeh blur near a tile boundary, the renderer needs pixels from outside the destination tile. This method computes how far that border region extends. Pass the returned rect’s origin as tileExtendOffset and allocate sourceTileRGBA with the returned rect’s size.

## Parameters

- `tileRect`: The destination tile rect in full-image pixel coordinates.
- `sourceRGBASize`: The dimensions of the full (un-tiled) source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnimagerenderingsession/minimumtileextendrect(fortilerect:sourcergbasize:))*