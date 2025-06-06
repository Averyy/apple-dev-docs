# randomTensor(withShapeTensor:descriptor:stateTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a Random op of type matching distribution in descriptor, and returns random values and updated state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func randomTensor(withShapeTensor shapeTensor: MPSGraphTensor, descriptor: MPSGraphRandomOpDescriptor, stateTensor state: MPSGraphTensor, name: String?) -> [MPSGraphTensor]
```

#### Return Value

An array of MPSGraphTensor of size 2. The first MPSGraphTensor is of shape containing random values in the defined range. The second MPSGraphTensor is the updated state tensor.

#### Discussion

Returns an array of 2 tensors, where the first is of provided shape of random values in the distribution specified, and the second is the updated state tensor. Uses the provided state to define a stream of random values. No state is preserved, and all calls with equal state yield an identical stream of random values. The initial stateTensor provided should be created using the MPSGraph randomPhiloxStateTensor APIs. The resulting stateTensor from this op can be passed as an argument to the following random calls to continue sampling from the stream.

## Parameters

- `shapeTensor`: 1D Int32 or Int64 tensor. The shape of the tensor generated.
- `descriptor`: The descriptor of the distribution. See MPSGraphRandomOpDescriptor.
- `state`: The state to define a stream of random values. All calls with equal state yield an identical stream of random values.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/randomtensor(withshapetensor:descriptor:statetensor:name:))*