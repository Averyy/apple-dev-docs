# init(type:location:)

**Framework**: RealityKit  
**Kind**: init

Creates an accessory anchoring source for a deferred accessory type.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(type: AnchoringComponent.AccessoryAnchoringSource.AccessoryType, location: String? = nil)
```

#### Discussion

Use this initializer when you want to anchor to an accessory that may not be connected yet. The system will automatically bind to a matching accessory when it connects.

## Parameters

- `type`: The type of accessory to anchor to (e.g., `.leftController`, `.stylus`)
- `location`: Optional location name on the accessory (e.g., “aim”, “grip”, “tip”). If `nil` or empty, anchors to the accessory’s origin. If the specified location doesn’t exist at runtime, falls back to origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/accessoryanchoringsource/init(type:location:))*