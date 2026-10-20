# CIRenderDestinationAlphaMode

**Framework**: Core Image  
**Kind**: enum  
**Role**: Enumeration

Different ways of representing alpha.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum CIRenderDestinationAlphaMode
```

```c
enum CIRenderDestinationAlphaMode : NSUInteger;
```

## Topics

### Enumeration Cases
- [CIRenderDestinationAlphaMode.none](./cirenderdestinationalphamode/none.md)
  Designates a destination with no alpha compositing.
- [CIRenderDestinationAlphaMode.premultiplied](./cirenderdestinationalphamode/premultiplied.md)
  Designates a destination that expects premultiplied alpha values.
- [CIRenderDestinationAlphaMode.unpremultiplied](./cirenderdestinationalphamode/unpremultiplied.md)
  Designates a destination that expects non-premultiplied alpha values.
### Initializers
- [init?(rawValue: UInt)](./cirenderdestinationalphamode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Custom Render Destination
- [Generating an animation with a Core Image Render Destination](./generating-an-animation-with-a-core-image-render-destination.md)
  Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [class CIRenderDestination](./cirenderdestination.md)
  A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.
- [class CIRenderInfo](./cirenderinfo.md)
  An encapsulation of a render task’s timing, passes, and pixels processed.
- [class CIRenderTask](./cirendertask.md)
  A single render task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestinationalphamode)*