# CNImageRenderingSessionConfiguration

**Framework**: Cinematic  
**Kind**: class

Configuration for a CNImageRenderingSession, specifying the rendering quality and algorithm version.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
class CNImageRenderingSessionConfiguration
```

## Topics

### Initializers
- [init(quality: CNRenderingQuality)](cnimagerenderingsessionconfiguration/init(quality:).md)
  Initialize with the latest rendering version
- [init?(quality: CNRenderingQuality, renderingVersion: Int)](cnimagerenderingsessionconfiguration/init(quality:renderingversion:).md)
  Initialize with a specific rendering version.
### Instance Properties
- [var quality: CNRenderingQuality](cnimagerenderingsessionconfiguration/quality.md)
- [var renderingVersion: Int](cnimagerenderingsessionconfiguration/renderingversion.md)
  Rendering version used to render
### Type Properties
- [class var latestRenderingVersion: Int](cnimagerenderingsessionconfiguration/latestrenderingversion.md)
  The version of the newest rendering algorithm
### Type Methods
- [class func isRenderingVersionSupported(Int) -> Bool](cnimagerenderingsessionconfiguration/isrenderingversionsupported(_:).md)
  Checks if a given rendering version is supported on the current build

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnimagerenderingsessionconfiguration)*