# AudioUnitRenderContext

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

A structure that contains thread context information for a real-time rendering operation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```c
struct AudioUnitRenderContext;
```

## Mentions

- [Adding Audio Unit Auxiliary Real-Time Threads to Audio Workgroups](./adding-audio-unit-auxiliary-real-time-threads-to-audio-workgroups.md)

## Overview

When the thread context of a rendering operation changes, the system packages the new rendering context information in an [`AudioUnitRenderContext`](./audiounitrendercontext.md) structure and passes it to the [`AURenderContextObserver`](./aurendercontextobserver.md) block of any associated Audio Unit app extensions.

## Topics

### Properties
- [workgroup](./audiounitrendercontext/workgroup.md)
  The workgroup that manages the rendering threads of the audio unit.
- [reserved](./audiounitrendercontext/reserved.md)
  System-specific information.

## See Also

### Host App Workgroup
- [kAudioUnitProperty_RenderContextObserver](./kaudiounitproperty_rendercontextobserver.md)
  The block that the system calls when the rendering context changes.
- [AURenderContextObserver](./aurendercontextobserver.md)
  A custom block that tells the audio unit which thread context to use for the next render cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitrendercontext)*