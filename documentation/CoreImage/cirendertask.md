# CIRenderTask

**Framework**: Core Image  
**Kind**: class

A single render task.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIRenderTask
```

#### Overview

A single render task issued in conjunction with [`CIRenderDestination`](cirenderdestination.md).

A `CIRenderTask` object appears in Xcode Quick Look as a graph.

## Topics

### Instance Methods
- [func waitUntilCompleted() throws -> CIRenderInfo](cirendertask/waituntilcompleted.md)
  Waits until the [`CIRenderTask`](cirendertask.md) finishes and returns.
### Instance Properties
- [var plannedPassCount: Int](cirendertask/plannedpasscount.md)
- [var plannedPeakMemory: Int](cirendertask/plannedpeakmemory.md)
- [var plannedPixelsOverdrawn: Int](cirendertask/plannedpixelsoverdrawn.md)
- [var plannedPixelsProcessed: Int](cirendertask/plannedpixelsprocessed.md)

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

## See Also

- [Generating an animation with a Core Image Render Destination](generating-an-animation-with-a-core-image-render-destination.md)
  Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [class CIRenderDestination](cirenderdestination.md)
  A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.
- [class CIRenderInfo](cirenderinfo.md)
  An encapsulation of a render task’s timing, passes, and pixels processed.
- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirendertask)*