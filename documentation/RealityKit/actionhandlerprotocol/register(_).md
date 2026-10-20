# register(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method  
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

## Default Implementations

### ActionHandlerProtocol Implementations
- [static func register((Self.EventType) -> (any ActionHandlerProtocol)?)](./register%28_%29-1jigj.md)
  Registers a handler that creates an action handler, and subscribes to one or more events.
- [static func register((Self.EventType) -> (any ActionHandlerProtocol)?)](./register%28_%29-1kxs4.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionhandlerprotocol/register(_:))*