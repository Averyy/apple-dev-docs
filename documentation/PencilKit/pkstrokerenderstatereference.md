# PKStrokeRenderStateReference

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

An object that captures the render-time state of a stroke, such as grain texture position.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class PKStrokeRenderStateReference
```

```objc
@interface PKStrokeRenderState : NSObject
```

#### Overview

`PKStrokeRenderState` is the Objective-C representation of a stroke’s rendering context. It conforms to `NSCopying` and `NSSecureCoding` for archiving. In Swift, use the equivalent value type [`PKStroke.RenderState`](./pkstroke-swift.struct/renderstate-swift.struct.md) instead.

## Topics

### Getting the render state
- [var grainOffset: CGPoint](./pkstrokerenderstatereference/grainoffset.md)
  The pre-transform position of the grain texture for strokes with a backing grain texture such as crayon.
### Using Swift types
- [PKStroke.RenderState](./pkstroke-swift.struct/renderstate-swift.struct.md)
  A value that captures the render-time state of a stroke, such as grain texture position.
### Initializers
- [convenience init(PKStroke.RenderState)](./pkstrokerenderstatereference/init%28_%29.md)
  Creates a `PKStrokeRenderStateReference` from its Swift counterpart `PKStroke.RenderState`.
- [init?(coder: NSCoder)](./pkstrokerenderstatereference/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerenderstatereference)*