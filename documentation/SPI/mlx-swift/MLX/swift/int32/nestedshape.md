---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/swift/int32/nestedshape"
framework: "mlx-swift/MLX"
---

# nestedShape

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Instance Property

The shape of the receiver.

## Declaration

```swift
var nestedShape: [Int] { get }
```

Available when `Self` conforms to `HasDType`.

## Discussion

Note: the nesting must be rectangular – every element at a given level must have the same shape – or the precondition will fail.

Note: an empty level says nothing about the levels below it, so those are reported as `0` – `[[Int]]()` has shape `[0, 0]`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/swift/int32/nestedshape)*