# CNImageRenderingSession

**Framework**: Cinematic  
**Kind**: class

A session for rendering a shallow depth-of-field (SDoF) effect onto still images using Metal.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
class CNImageRenderingSession
```

#### Overview

Use CNImageRenderingSession to apply a cinematic, lens-simulated bokeh effect to an image given a disparity map. For large images, prefer the tiled API to avoid excessive GPU memory usage.

A single session may be reused across multiple render calls. It is not thread-safe.

## Topics

### Initializers
- [init(configuration: CNImageRenderingSessionConfiguration)](cnimagerenderingsession/init(configuration:).md)
### Instance Properties
- [var configuration: CNImageRenderingSessionConfiguration](cnimagerenderingsession/configuration.md)
### Instance Methods
- [func encodeRender(to: any MTLCommandBuffer, sourceRGBA: any MTLTexture, sourceDisparity: any MTLTexture, destinationRGBA: any MTLTexture, fNumber: Float, focusDisparity: Float) -> Bool](cnimagerenderingsession/encoderender(to:sourcergba:sourcedisparity:destinationrgba:fnumber:focusdisparity:).md)
  Encode a command to render a shallow depth of field (SDoF) image to a metal texture
- [func encodeTileRender(to: any MTLCommandBuffer, sourceTileRGBA: any MTLTexture, sourceDisparity: any MTLTexture, destinationTileRGBA: any MTLTexture, fNumber: Float, focusDisparity: Float, sourceRGBASize: CGSize, tileOffset: CGPoint, tileExtendOffset: CGPoint) -> Bool](cnimagerenderingsession/encodetilerender(to:sourcetilergba:sourcedisparity:destinationtilergba:fnumber:focusdisparity:sourcergbasize:tileoffset:tileextendoffset:).md)
  Encode a command to render a shallow depth of field (SDoF) image to a metal texture
### Type Methods
- [class func minimumTileExtendRect(forTileRect: CGRect, sourceRGBASize: CGSize) -> CGRect](cnimagerenderingsession/minimumtileextendrect(fortilerect:sourcergbasize:).md)
  Returns the minimum source rect that must be sampled to render tileRect without edge artifacts.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnimagerenderingsession)*