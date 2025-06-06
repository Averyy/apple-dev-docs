# setProperties(_:)

**Framework**: Model I/O  
**Kind**: method

Sets the material property’s attributes to those of the specified material property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setProperties(_ property: MDLMaterialProperty)
```

#### Discussion

Use this method to copy data from one [`MDLMaterialProperty`](mdlmaterialproperty.md) instance to another—for example, to make one material property of a [`MDLScatteringFunction`](mdlscatteringfunction.md) object match the value of another.

## Parameters

- `property`: The material property from which to copy data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialproperty/setproperties(_:))*