# init(device:)

**Framework**: RealityKit  
**Kind**: init

Creates the accessory anchoring source by the GCDevice asynchronously Returns an AccessoryAnchoringSource if the GCDevice supports spatial tracking, throwing an error otherwise

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(device: any GCDevice) async throws
```

## Parameters

- `device`: Device to track


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/accessoryanchoringsource/init(device:))*