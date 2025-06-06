# init(componentNoises:selectionNoise:)

**Framework**: GameplayKit  
**Kind**: init

Creates a noise object by combining the specified noise objects, using another noise object to select which regions of the output correspond to which input noise.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(componentNoises noises: [GKNoise], selectionNoise: GKNoise)
```

#### Return Value

A new noise object.

#### Discussion

This method is equivalent to the [`init(componentNoises:selectionNoise:componentBoundaries:boundaryBlendDistances:)`](gknoise/init(componentnoises:selectionnoise:componentboundaries:boundaryblenddistances:).md) method, but automatically determines uniformly spaced boundaries based on the number of noise objects in the `noises` array, and using a blend distance of zero for each boundary. Together with these boundaries, the `selectionNoise` parameter determines which of the input noise objects appears in which region of generated noise.

For example, if the `noises` array contains two noise objects, the boundary value is zero: In regions where the `selectionNoise` field has negative values, the noise created by this method uses values from the first element of the `noises` array, and in regions where the `selectionNoise` field has positive values, the created noise uses values from the second element in the `noises` array.

![None](https://docs-assets.developer.apple.com/published/e17af09b72dc79daddb55ae834daf642/media-2556365%402x.png)

## Parameters

- `noises`: The array of noise objects to combine.
- `selectionNoise`: A noise object whose values determine which object from the   array contributes to which region of the generated output.

## See Also

- [convenience init(componentNoises: [GKNoise], selectionNoise: GKNoise, componentBoundaries: [NSNumber], boundaryBlendDistances: [NSNumber])](gknoise/init(componentnoises:selectionnoise:componentboundaries:boundaryblenddistances:).md)
  Creates a noise object by combining the specified noise objects, using another noise object and the specified boundaries to select which regions of the output correspond to which input noise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/init(componentnoises:selectionnoise:))*