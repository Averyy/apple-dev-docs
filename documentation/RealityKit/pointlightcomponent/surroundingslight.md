# PointLightComponent.SurroundingsLight

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A component that specifies that the point light illuminates the physical and immersive environment.

**Availability**:
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SurroundingsLight
```

## Performance Considerations

Set [`attenuationRadius`](./attenuationradius.md) deliberately on lights that use this component. Its default is often larger than needed, and the resulting on-screen footprint is the dominant driver of this effect’s cost.

The cost depends on how many pixels receive this effect, which is why attenuation radius is important. There is also a cost for each light that is in each pixel.

Excessive use of this effect may contribute to user-noticeable frame drops and can cause the device to heat up in graphically demanding situations. Monitor the thermal state and  usage as a mitigation, if necessary. Apps can monitor thermal state changes by subscribing to the [`thermalStateDidChange`](../../Foundation/notificationcenter/messageidentifier/thermalstatedidchange.md) notification.

To stay responsive to the device’s available thermal headroom, read [`thermalState`](../../Foundation/processinfo/thermalstate-swift.property.md) and observe [`thermalStateDidChange`](../../Foundation/notificationcenter/messageidentifier/thermalstatedidchange.md) to react when it changes. As the reported state moves from `.fair` toward `.serious` and `.critical`, reduce the attenuation radius, or remove this component from lights where the effect is not essential.

## Topics

### Initializers
- [init()](./surroundingslight/init%28%29.md)
  Creates a surroundings light component.

## Relationships

### Conforms To
- [Component](../component.md)
- [Equatable](../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/pointlightcomponent/surroundingslight)*