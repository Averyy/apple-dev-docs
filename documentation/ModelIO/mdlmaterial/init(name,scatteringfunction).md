# init(name:scatteringFunction:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

Initializes a material

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(name: String, scatteringFunction: MDLScatteringFunction)
```

```objc
- (instancetype) initWithName:(NSString *) name scatteringFunction:(MDLScatteringFunction *) scatteringFunction;
```

## Return Value

A new material object.

## Discussion

To use the newly created material with a 3D object, assign it to the the [`material`](../mdlsubmesh/material.md) property of a [`MDLSubmesh`](../mdlsubmesh.md) instance.

## Parameters

- `name`: A descriptive name for the material.
- `scatteringFunction`: The collection of material properties that define the material’s response to light. For details, see the [`scatteringFunction`](./scatteringfunction.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/init(name:scatteringfunction:))*