# allowCrossing

**Framework**: RealityKit  
**Kind**: property

An option that enables the crossing feature.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
static let allowCrossing: PortalComponent.Options
```

#### Discussion

Objects within the portal world with a [`PortalCrossingComponent`](portalcrossingcomponent.md) can cross the portal when the `allowCrossing` option is in an enabled state. Crossing behavior is based on the user-defined geometry for [`crossingMode`](portalcomponent/crossingmode-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/options/allowcrossing)*