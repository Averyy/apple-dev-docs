# compatibilityWith(_:)

**Framework**: RealityKit  
**Kind**: method

Compares network compatibility tokens between the local device and another device.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
final func compatibilityWith(_ otherToken: NetworkCompatibilityToken) -> NetworkCompatibilityToken.Compatibility
```

#### Return Value

Returns [`NetworkCompatibilityToken.Compatibility.compatible`](networkcompatibilitytoken/compatibility/compatible.md) if the local client and the remote client represented by `otherToken` can be synced. Any other result indicates that the two devices are incompatible and you shouldn’t proceed with the connection.

## Parameters

- `otherToken`: The token for the remote client against which the local   device checks compatibility


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken/compatibilitywith(_:))*