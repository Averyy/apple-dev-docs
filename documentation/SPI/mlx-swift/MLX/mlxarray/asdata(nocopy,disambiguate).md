---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/asdata(nocopy:disambiguate:)"
framework: "mlx-swift/MLX"
---

# asData(noCopy:disambiguate:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Return the contents as contiguous bytes in the native [`dtype`](./dtype.md).

> **Deprecated**: use asData(acccess: .copy)

## Declaration

```swift
func asData(noCopy: Bool = false, disambiguate: Bool = false) -> Data
```

## Discussion

> **Note**: If you can guarantee the lifetime of the [`MLXArray`](../mlxarray.md) will exceed the Data and that the array will not be mutated (e.g. using indexing or other means) it is possible to pass `noCopy: true` to reference the backing bytes.

**Replaced with** [`asData(access:)`](./asdata%28access%29.md)

### See Also

- [Conversion](../conversion.md)
- [`asArray(_:)`](./asarray%28_%29.md)
- [`asMTLBuffer(device:noCopy:)`](./asmtlbuffer%28device,nocopy%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/asdata(nocopy:disambiguate:))*