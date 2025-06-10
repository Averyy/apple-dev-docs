# graphBuilderTensor(_:)

**Framework**: Swift  
**Kind**: method

Returns a tensor for the specified BNNS Graph builder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func graphBuilderTensor(_ builder: BNNSGraph.Builder) -> BNNSGraph.Builder.Tensor<Element>
```

#### Discussion

The following code shows how to use this function to register a tensor from an unsafe mutable buffer pointe:.

```swift
   var xValues = [1, 2, 3, 4] as [Float]
   var yValues = [5, 6, 7, 8] as [Float]

   let context = try BNNSGraph.makeContext {
       builder in

       xValues.withUnsafeMutableBufferPointer { xPtr in
           yValues.withUnsafeMutableBufferPointer { yPtr in

               let x = xPtr.graphBuilderTensor(builder)

               let z = x.matmul(transpose: true,
                                other: yPtr)

               return [z] // On return, `z[0]` equals `70`.
           }
       }
   }
```

> **Note**: This function copies the values in `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/graphbuildertensor(_:))*