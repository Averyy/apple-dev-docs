---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:_:)-798zt"
framework: "mlx-swift/MLX"
---

# init(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of `MLXArray` from a buffer of `HasDType` values with an optional shape.

## Declaration

```swift
convenience init<T>(_ ptr: UnsafeBufferPointer<T>, _ shape: (some Collection<Int>)? = [Int]?.none) where T : HasDType
```

#### Discussion

```swift
let image = vImage.PixelBuffer
let array = image.withUnsafeBufferPointer { ptr in
    MLXArray(ptr, [64, 64, 4])
}
```

##### See Also

- [Initialization](../initialization.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:_:)-798zt)*