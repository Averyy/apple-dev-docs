# graphBuilderTensor(_:)

**Framework**: Swift  
**Kind**: method

Returns a tensor for the specified BNNS Graph builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func graphBuilderTensor(_ builder: BNNSGraph.Builder) -> BNNSGraph.Builder.Tensor<Element>
```

#### Discussion

The following code shows how to use this function to register a tensor from an array slice.

```swift
   let x = ([0, 1, 2, 3, 4, 5] as [Float])[1...4]
   let y = ([4, 5, 6, 7, 8, 9] as [Float])[1...4]

   let context = try BNNSGraph.makeContext {
       builder in

       let x = x.graphBuilderTensor(builder)

       let z = x.matmul(transpose: true,
                        other: y)

       return [z] // On return, `z[0]` equals `70`.
   }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/arrayslice/graphbuildertensor(_:))*