# PKStrokeRenderStateReference

**Framework**: PencilKit  
**Kind**: class

An object that captures the render-time state of a stroke, such as grain texture position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class PKStrokeRenderStateReference
```

#### Overview

`PKStrokeRenderState` is the Objective-C representation of a stroke’s rendering context. It conforms to `NSCopying` and `NSSecureCoding` for archiving. In Swift, use the equivalent value type [`PKStroke.RenderState`](pkstroke-swift.struct/renderstate-swift.struct.md) instead.

## Topics

### Getting the render state
- [var grainOffset: CGPoint](pkstrokerenderstatereference/grainoffset.md)
  The pre-transform position of the grain texture for strokes with a backing grain texture such as crayon.
### Using Swift types
- [PKStroke.RenderState](pkstroke-swift.struct/renderstate-swift.struct.md)
  A value that captures the render-time state of a stroke, such as grain texture position.
### Initializers
- [convenience init(PKStroke.RenderState)](pkstrokerenderstatereference/init(_:).md)
  Creates a `PKStrokeRenderStateReference` from its Swift counterpart `PKStroke.RenderState`.
- [init?(coder: NSCoder)](pkstrokerenderstatereference/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerenderstatereference)*