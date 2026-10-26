# register(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

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

Available when `ActionType` conforms to `Decodable`, `ActionType` conforms to `Encodable`, `ActionType.EventParameterType` conforms to `Decodable`, and `ActionType.EventParameterType` conforms to `Encodable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionhandlerprotocol/register(_:)-1kxs4)*