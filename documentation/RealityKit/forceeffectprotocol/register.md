# register(_:)

**Framework**: RealityKit  
**Kind**: method

Registers the custom effect.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency static func register(_ updateHandler: (@MainActor (inout ForceEffectEvent<Self>) -> Void)? = nil)
```

#### Discussion

If a handler is specified, the physics system calls the handler and ignores the update function.

## Parameters

- `updateHandler`: A closure that computes custom forces for rigid bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectprotocol/register(_:))*