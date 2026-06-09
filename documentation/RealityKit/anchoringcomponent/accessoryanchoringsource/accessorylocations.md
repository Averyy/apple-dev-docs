# accessoryLocations

**Framework**: RealityKit  
**Kind**: property

The list of anchor-able locations for this accessory.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var accessoryLocations: [AnchoringComponent.AccessoryLocation] { get }
```

#### Discussion

The returned array is device-specific; its contents are defined by the accessory’s manufacturer, and may or may not include [`origin`](anchoringcomponent/accessorylocation/origin.md). [`origin`](anchoringcomponent/accessorylocation/origin.md) is supported by every accessory and is always available via the static property, regardless of whether it appears in this array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/accessoryanchoringsource/accessorylocations)*