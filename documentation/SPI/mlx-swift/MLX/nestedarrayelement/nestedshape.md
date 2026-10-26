---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nestedarrayelement/nestedshape"
framework: "mlx-swift/MLX"
---

# nestedShape

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The shape of the receiver.

## Declaration

```swift
var nestedShape: [Int] { get }
```

#### Discussion

Note: the nesting must be rectangular – every element at a given level must have the same shape – or the precondition will fail.

Note: an empty level says nothing about the levels below it, so those are reported as `0` – `[[Int]]()` has shape `[0, 0]`.

## Default Implementations

### NestedArrayElement Implementations
- [var nestedShape: [Int]](./nestedshape-9q06q.md)
  The shape of the receiver.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nestedarrayelement/nestedshape)*