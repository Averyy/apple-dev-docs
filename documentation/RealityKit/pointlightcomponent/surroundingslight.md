# PointLightComponent.SurroundingsLight

**Framework**: RealityKit  
**Kind**: struct

A component that specifies that the point light illuminates the physical and immersive environment.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SurroundingsLight
```

#### Performance Considerations

Set [`attenuationRadius`](pointlightcomponent/attenuationradius.md) deliberately on lights that use this component. Its default is often larger than needed, and the resulting on-screen footprint is the dominant driver of this effect’s cost.

The cost depends on how many pixels receive this effect, which is why attenuation radius is important. There is also a cost for each light that is in each pixel.

Excessive use of this effect may contribute to user-noticeable frame drops and can cause the device to heat up in graphically demanding situations. Monitor the thermal state and  usage as a mitigation, if necessary. Apps can monitor thermal state changes by subscribing to the [`thermalStateDidChange`](https://developer.apple.com/documentation/Foundation/NotificationCenter/MessageIdentifier/thermalStateDidChange) notification.

To stay responsive to the device’s available thermal headroom, read [`thermalState`](https://developer.apple.com/documentation/Foundation/ProcessInfo/thermalState-swift.property) and observe [`thermalStateDidChange`](https://developer.apple.com/documentation/Foundation/NotificationCenter/MessageIdentifier/thermalStateDidChange) to react when it changes. As the reported state moves from `.fair` toward `.serious` and `.critical`, reduce the attenuation radius, or remove this component from lights where the effect is not essential.

## Topics

### Initializers
- [init()](pointlightcomponent/surroundingslight/init.md)
  Creates a surroundings light component.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/pointlightcomponent/surroundingslight)*