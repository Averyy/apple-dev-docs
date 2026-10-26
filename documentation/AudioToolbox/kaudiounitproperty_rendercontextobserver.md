# kAudioUnitProperty_RenderContextObserver

**Framework**: Audio Toolbox  
**Kind**: case  
**Role**: Enumeration Case

The block that the system calls when the rendering context changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```c
kAudioUnitProperty_RenderContextObserver
```

#### Discussion

If your Audio Unit creates auxilliary realtime rendering threads, set the value of this key to the [`AURenderContextObserver`](./aurendercontextobserver.md) block you want the system to execute. The system executes your block when the rendering context changes.

> ❗ **Important**:  The block you provide is for system use only. Audio Unit hosts must not attempt to interact with the audio unit through this block.

## See Also

### Host App Workgroup
- [AURenderContextObserver](./aurendercontextobserver.md)
  A custom block that tells the audio unit which thread context to use for the next render cycle.
- [AudioUnitRenderContext](./audiounitrendercontext.md)
  A structure that contains thread context information for a real-time rendering operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_rendercontextobserver)*