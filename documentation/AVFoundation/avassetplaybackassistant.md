# AVAssetPlaybackAssistant

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that provides playback information for an asset.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class AVAssetPlaybackAssistant
```

```objc
@interface AVAssetPlaybackAssistant : NSObject
```

## Topics

### Creating a playback assistant
- [convenience init(asset: AVAsset)](./avassetplaybackassistant/init%28asset%29.md)
  Creates a playback assistant to inspect the specified asset.
### Loading playback configuration options
- [func loadPlaybackConfigurationOptions(completionHandler: ([AVAssetPlaybackConfigurationOption]) -> Void)](./avassetplaybackassistant/loadplaybackconfigurationoptions%28completionhandler%29.md)
  Loads playback configuration options for an asset.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Utilities
- [struct AVAssetPlaybackConfigurationOption](./avassetplaybackconfigurationoption.md)
  A structure that defines playback configuration options for an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetplaybackassistant)*