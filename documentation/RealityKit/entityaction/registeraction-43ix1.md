# registerAction()

**Framework**: RealityKit  
**Kind**: method

Registers the serializable action into the action-types registry.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static func registerAction()
```

#### Discussion

Registering an action allows RealityKit to retrieve its [`AnimationResource`](animationresource.md) definitions.

Registering an action may not be necessary, because RealityKit automatically registers the action when you:

- Initialize an [`ActionAnimation`](actionanimation.md) with this action.
- Subscribe to it in any way, including subscribing an [`ActionHandlerProtocol`](actionhandlerprotocol.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entityaction/registeraction()-43ix1)*