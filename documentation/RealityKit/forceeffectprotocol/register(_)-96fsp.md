# register(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Register the codable custom effect. If a handler is specified, the closure is used to update the effect.

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

Available when `Self` conforms to `Decodable` and `Encodable`.

**Other overloads**:

```swift
@MainActor
@preconcurrency static func register(_ updateHandler: (@MainActor (inout ForceEffectEvent<Self>) -> Void)? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectprotocol/register(_:)-96fsp)*