# constant(name:value:)

**Framework**: Accelerate  
**Kind**: method

Registers and returns a tensor that contains a constant scalar value.

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
func constant<T>(name: String? = nil, value: T) -> BNNSGraph.Builder.Tensor<T> where T : BNNSScalar
```

#### Discussion

For example, the following code defines the tensor `x` that contains the single-precision scalar value `10.0`:

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
- `value`: The scalar value that the function copies into the compiled context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/constant(name:value:))*