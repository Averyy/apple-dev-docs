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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerenderstatereference)*