# PHASEEngine.RenderingMode

**Framework**: PHASE  
**Kind**: enum

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum RenderingMode
```

#### Overview

```None
A local engine is connected to an audio device and renders audio in real-time in the application process.
In this mode the engine receives all its inputs from the client such as acoustic configuration.
Updating an engine configured with `PHASERenderingModeLocal` executes any pending API commands locally.
```

```None
A client engine is connected to an audio device and renders audio in real-time in a secure process.
In this mode the engine receives inputs from the client and renders in a server.
In supported platforms this allows the server to apply privacy sensitive effects such as room virtual acoustics, low latency head-tracking and personalized Spatial Audio.
Updating an engine configured with `PHASERenderingModeClient` syncs any pending API commands to the server for processing.
```

## Topics

### Enumeration Cases
- [PHASEEngine.RenderingMode.client](phaseengine/renderingmode/client.md)
- [PHASEEngine.RenderingMode.local](phaseengine/renderingmode/local.md)
### Initializers
- [init?(rawValue: Int)](phaseengine/renderingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/renderingmode)*