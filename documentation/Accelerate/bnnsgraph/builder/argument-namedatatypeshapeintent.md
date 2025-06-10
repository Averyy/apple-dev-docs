# argument(name:dataType:shape:intent:)

**Framework**: Accelerate  
**Kind**: method

Registers and returns an input or in-out tensor argument to the graph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func argument<T>(name: String? = nil, dataType: T.Type, shape: [Int], intent: BNNSGraph.Builder.Intent = .input) -> BNNSGraph.Builder.Tensor<T> where T : BNNSScalar
```

#### Discussion

The following code shows how to specify inputs with flexible shapes. The code calls `setBatchSize` before executing the context to specify that the two inputs and the output tensors are 8-element vectors:

```None
       let context = try? BNNSGraph.makeContext ({
           builder in

           let x = builder.argument(name: "x",
                                    dataType: Float.self,
                                    shape: [-1])
           let y = builder.argument(name: "y",
                                    dataType: Float.self,
                                    shape: [-1])

           let z = x + y

           return [z]
       })

       var args = context.argumentNames().map {
           name in

           return context.tensor(argument: name,
                                 fillKnownDynamicShapes: false)!
       }

       defer {
           args.forEach {
               $0.deallocate()
           }
       }

       let n = 8

       context.setBatchSize(n)

       args[context.argumentPosition(argument: "x")]
           .allocate(initializingFrom: [1, 2, 3, 4, 5, 6, 7, 8] as [Float])

       args[context.argumentPosition(argument: "y")]
           .allocate(initializingFrom: [10, 20, 30, 40, 50, 60, 70, 80] as [Float])

       // Output argument
       args[0].allocate(as: Float.self, count: n)

       try context.executeFunction(arguments: &args)
       ```
On return, the output tensor contains the values `[11, 22, 33, 44, 55, 66, 77, 88]`.
```

## Parameters

- `name`: The name of the argument.
- `dataType`: The argument’s data type.
- `shape`: An array of integers or closed ranges that define the sizes of each   dimension of the argument. Pass a negative value to specify a flexible dimension.
- `intent`: A constant that specifies whether the argument is input, output, or in-out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/argument(name:datatype:shape:intent:))*