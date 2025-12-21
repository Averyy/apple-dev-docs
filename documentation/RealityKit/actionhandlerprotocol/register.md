# register(_:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Registers a handler that responds to raised action events for a particular action type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static func register(_ creationHandler: @escaping (Self.EventType) -> (any ActionHandlerProtocol)?)
```

## Parameters

- `creationHandler`: The closure that instantiates the handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionhandlerprotocol/register(_:))*