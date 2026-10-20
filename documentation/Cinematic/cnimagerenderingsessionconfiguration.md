# CNImageRenderingSessionConfiguration

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

Configuration for a CNImageRenderingSession, specifying the rendering quality and algorithm version.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class CNImageRenderingSessionConfiguration
```

```objc
@interface CNImageRenderingSessionConfiguration : NSObject
```

## Topics

### Initializers
- [init(quality: CNRenderingQuality)](./cnimagerenderingsessionconfiguration/init%28quality%29.md)
  Initialize with the latest rendering version
- [init?(quality: CNRenderingQuality, renderingVersion: Int)](./cnimagerenderingsessionconfiguration/init%28quality,renderingversion%29.md)
  Initialize with a specific rendering version.
### Instance Properties
- [var quality: CNRenderingQuality](./cnimagerenderingsessionconfiguration/quality.md)
- [var renderingVersion: Int](./cnimagerenderingsessionconfiguration/renderingversion.md)
  Rendering version used to render
### Type Properties
- [class var latestRenderingVersion: Int](./cnimagerenderingsessionconfiguration/latestrenderingversion.md)
  The version of the newest rendering algorithm
### Type Methods
- [class func isRenderingVersionSupported(Int) -> Bool](./cnimagerenderingsessionconfiguration/isrenderingversionsupported%28_%29.md)
  Checks if a given rendering version is supported on the current build

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

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnimagerenderingsessionconfiguration)*