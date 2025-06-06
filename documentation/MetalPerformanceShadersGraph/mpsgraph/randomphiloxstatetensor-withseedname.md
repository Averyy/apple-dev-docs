# randomPhiloxStateTensor(withSeed:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a tensor representing state using the Philox algorithm with given counter and key values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func randomPhiloxStateTensor(withSeed seed: Int, name: String?) -> MPSGraphTensor
```

#### Discussion

Generates random numbers using the Philox counter-based algorithm, for further details see: John K. Salmon, Mark A. Moraes, Ron O. Dror, and David E. Shaw. Parallel Random Numbers: As Easy as 1, 2, 3. A stateTensor generated with this API can be used in MPSGraph Random APIs which accept a stateTensor. The updated stateTensor is returned alongside the random values, and can be fed to the following random layer. In most use cases, a stateTensor should only need to be initialized once at the start of the graph. A stateTensor can be set as a target tensor of an MPSGraph execution to obtain a stateTensor serialized as an NDArray. This can be used as input to a placeholder in the graph to avoid ever needing to have a state intilization layer in an MPSGraph. This can allow for a continued stream through multiple executions of a single MPSGraph by having the final stateTensor as a target tensor passed into the following MPSGraph execution as a placeholder input. This may be helpful for training graphs in particular.

```md
MPSGraph *graph = [MPSGraph new]; 
MPSGraphTensor *stateTensor = [graph randomPhiloxStateTensorWithSeed: seed name: nil]; 
NSArray<MPSGraphTensor*> *resultTensors0 = [graph randomUniformTensorWithShape:

- Parameters:
  - seed: Initial counter and key values will be generated using seed.
  - name: Name for the operation
- Returns: An MPSGraphTensor representing a random state, to be passed as an input to a random op.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/randomphiloxstatetensor(withseed:name:))*