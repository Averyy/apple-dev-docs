# isEnabled

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the node is casting light.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

## Discussion

If the value is [`true`](../../Swift/true.md), the light is enabled and affects sprite nodes in the scene. The default is [`true`](../../Swift/true.md).

## See Also

### Determining Whether a Light Node Is Active
- [var categoryBitMask: UInt32](./categorybitmask.md)
  A mask that defines which categories this light belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklightnode/isenabled)*