# constant(name:values:shape:)

**Framework**: Accelerate  
**Kind**: method

Registers and returns a tensor with the specified shape that contains constant data, such as weight or bias values.

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
func constant<T>(name: String? = nil, values: some AccelerateBuffer, shape: [Int]? = nil) -> BNNSGraph.Builder.Tensor<T> where T : BNNSScalar
```

#### Discussion

For example, the following code defines the tensor `y` that contains the single-precision values `[1, 2, 3, 4, 5, 6, 7, 8]`:

```None
       let context = try BNNSGraph.makeContext ({
           builder in

           let x = builder.constant(name: "x",
                                    value : Float(10))
           let y = builder.constant(name: "y",
                                    values : [1, 2, 3, 4, 5, 6, 7, 8] as [Float])

           let z = x + y

           return [z]
       })

       var results = [context.allocateTensor(argument: context.argumentNames()[0],
                                               fillKnownDynamicShapes: false)!]
       defer {
           results[0].deallocate()
       }
       try context.executeFunction(arguments: &results)
```

On return, the `results[0]` tensor contains the values `[11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0]`.

## Parameters

- `name`: The name of the tensor.
- `values`: The tensor values that the function copies into the compiled context.
- `shape`: An array of integers that define the sizes of each dimension of the tensor. Set to    to specify that this function returns a vector that countains   elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/constant(name:values:shape:))*