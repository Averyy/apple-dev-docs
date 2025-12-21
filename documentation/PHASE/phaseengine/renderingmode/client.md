# PHASEEngine.RenderingMode.client

**Framework**: PHASE  
**Kind**: case

A mode that instructs the system to render audio in a secure process.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case client
```

#### Discussion

In this mode, the engine is connected to an audio device and renders audio in real-time in a secure process. The engine receives inputs from the client and renders in a server. Updating an engine that has a `client` configuration syncs pending API commands with the server for processing.

## See Also

- [PHASEEngine.RenderingMode.local](phaseengine/renderingmode/local.md)
  A mode that indicates that the system renders audio in process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/renderingmode/client)*