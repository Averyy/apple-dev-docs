# AURenderContextObserver

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A custom block that tells the audio unit which thread context to use for the next render cycle.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```c
typedef void (^)(const struct AudioUnitRenderContext *) __attribute__((nonblocking)) AURenderContextObserver;
```

## Mentions

- [Adding Audio Unit Auxiliary Real-Time Threads to Audio Workgroups](./adding-audio-unit-auxiliary-real-time-threads-to-audio-workgroups.md)

## Discussion

Provide this block if your Audio Unit creates its own auxiliary real-time rendering threads and operates them in parallel with the host app’s rendering thread. For a v3 Audio Unit, assign your block to the [`renderContextObserver`](./auaudiounit/rendercontextobserver.md) property of your [`AUAudioUnit`](./auaudiounit.md) object. For a v2 Audio Unit, assign this block to the [`kAudioUnitProperty_RenderContextObserver`](./kaudiounitproperty_rendercontextobserver.md) property of the audio unit.

Use the implementation of your block to prepare your Audio Unit’s rendering threads. For example, use this block to remove the thread from its previous workgroup and join the new workgroup in the [`AudioUnitRenderContext`](./audiounitrendercontext.md) structure passed to the block. If the new render context does not correspond to a real-time operation, the new workgroup might be `NULL`.

The system fetches and caches this block when it opens the Audio Unit. When the render context changes, the system calls the block from the render thread before it issues any new render requests.

## See Also

### Host App Workgroup
- [kAudioUnitProperty_RenderContextObserver](./kaudiounitproperty_rendercontextobserver.md)
  The block that the system calls when the rendering context changes.
- [AudioUnitRenderContext](./audiounitrendercontext.md)
  A structure that contains thread context information for a real-time rendering operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aurendercontextobserver)*