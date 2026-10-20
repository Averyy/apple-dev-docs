# CNImageRenderingSession

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

A session for rendering a shallow depth-of-field (SDoF) effect onto still images using Metal.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class CNImageRenderingSession
```

```objc
@interface CNImageRenderingSession : NSObject
```

#### Overview

Use CNImageRenderingSession to apply a cinematic, lens-simulated bokeh effect to an image given a disparity map. For large images, prefer the tiled API to avoid excessive GPU memory usage.

A single session may be reused across multiple render calls. It is not thread-safe.

## Topics

### Initializers
- [init(configuration: CNImageRenderingSessionConfiguration)](./cnimagerenderingsession/init%28configuration%29.md)
### Instance Properties
- [var configuration: CNImageRenderingSessionConfiguration](./cnimagerenderingsession/configuration.md)
### Instance Methods
- [func encodeRender(to: any MTLCommandBuffer, sourceRGBA: any MTLTexture, sourceDisparity: any MTLTexture, destinationRGBA: any MTLTexture, fNumber: Float, focusDisparity: Float) -> Bool](./cnimagerenderingsession/encoderender%28to,sourcergba,sourcedisparity,destinationrgba,fnumber,focusdisparity%29.md)
  Encode a command to render a shallow depth of field (SDoF) image to a metal texture
- [func encodeTileRender(to: any MTLCommandBuffer, sourceTileRGBA: any MTLTexture, sourceDisparity: any MTLTexture, destinationTileRGBA: any MTLTexture, fNumber: Float, focusDisparity: Float, sourceRGBASize: CGSize, tileOffset: CGPoint, tileExtendOffset: CGPoint) -> Bool](./cnimagerenderingsession/encodetilerender%28to,sourcetilergba,sourcedisparity,destinationtilergba,fnumber,focusdisparity,sourcergbasize,tileoffset,tileextendoffset%29.md)
  Encode a command to render a shallow depth of field (SDoF) image to a metal texture
### Type Methods
- [class func minimumTileExtendRect(forTileRect: CGRect, sourceRGBASize: CGSize) -> CGRect](./cnimagerenderingsession/minimumtileextendrect%28fortilerect,sourcergbasize%29.md)
  Returns the minimum source rect that must be sampled to render tileRect without edge artifacts.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnimagerenderingsession)*