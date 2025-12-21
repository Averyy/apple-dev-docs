# PHASEEngine.RenderingMode.local

**Framework**: PHASE  
**Kind**: case

A mode that indicates that the system renders audio in process.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case local
```

#### Discussion

In this mode, the engine is connected to an audio device and renders audio in real-time in the application process. The engine receives all of its inputs, for example, acoustic configuration, from the client. Updating an engine that has a `local` configuration executes any pending API commands locally.

## See Also

- [PHASEEngine.RenderingMode.client](phaseengine/renderingmode/client.md)
  A mode that instructs the system to render audio in a secure process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/renderingmode/local)*