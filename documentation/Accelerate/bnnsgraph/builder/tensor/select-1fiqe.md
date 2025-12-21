# select(_:_:)

**Framework**: Accelerate  
**Kind**: method

Adds a tensor-tensor select operation to the current graph.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func select<U>(_ valueIfTrue: BNNSGraph.Builder.Tensor<U>, _ valueIfFalse: BNNSGraph.Builder.Tensor<U>) -> BNNSGraph.Builder.Tensor<U> where U : BNNSScalar
```

#### Discussion

For example, the following code returns the `valueIfTrue` elements when the corresponding elements in `z` are `true` and the elements in `valueIfFalse` when the corresponding elements in `z` are `false`:

```None
let ctx = try BNNSGraph.makeContext {

    builder in

    let z = builder.argument(dataType: Bool.self, shape: [8])

    let x = builder.argument(dataType: Float.self, shape: [8])
    let y = builder.argument(dataType: Float.self, shape: [8])

    let masked = z.select(x, y)

    return [ masked ]
}

let z = BNNSTensor.allocate(initializingFrom: [true, true, false, false,
                                               true, true, false, false],
                            shape: [8], stride: [1])

let x = BNNSTensor.allocate(initializingFrom: [1, 2, 3, 4, 5, 6, 7, 8] as [Float],
                            shape: [8], stride: [1])
let y = BNNSTensor.allocate(initializingFrom: [10, 20, 30, 40, 50, 60, 70, 80] as [Float],
                            shape: [8], stride: [1])

let tensor_tensor = BNNSTensor.allocateUninitialized(scalarType: Float.self, shape: [8], stride: [1])

var args = [tensor_tensor, tensor_scalar, scalar_tensor, z, x, y]

try ctx.executeFunction(arguments: &args)

// Prints "[1.0, 2.0, 30.0, 40.0, 5.0, 6.0, 70.0, 80.0]".
print(tensor_tensor.makeArray(of: Float.self))

```

## Parameters

- `valueIfTrue`: The values that the operation returns when the corresponding value in   is  .
- `valueIfFalse`: The values that the operation returns when the corresponding value in   is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/select(_:_:)-1fiqe)*