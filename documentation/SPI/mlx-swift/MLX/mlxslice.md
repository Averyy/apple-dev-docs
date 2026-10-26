---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxslice"
framework: "mlx-swift/MLX"
---

# MLXSlice

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Representation of a slice in [`MLXArray`](./mlxarray.md) indexing operations.

## Declaration

```swift
struct MLXSlice
```

#### Overview

This is typically not used directly – the various range expressions implement [`MLXArrayIndex`](./mlxarrayindex.md) and can produce these, e.g.

```swift
let a = MLXArray(...)

print(a[1 ..< 3])
print(a[.stride(to: 8, by: 2)])
```

##### See Also

- [Indexing](./indexing.md)
- [`stride(from:to:by:)`](./mlxarrayindex/stride%28from,to,by%29.md)

## Topics

### Initializers
- [init(start: Int32?, end: Int32?, stride: Int32?)](./mlxslice/init%28start,end,stride%29.md)
  Initialize an MLXSlice with its optional parameters.
### Instance Properties
- [var description: String](./mlxslice/description.md)
- [var isFull: Bool](./mlxslice/isfull.md)
  `true` if this is a full range (unrestricted) slice
- [var stride: Int32](./mlxslice/stride.md)
  Given `stride` or `1`
### Instance Methods
- [func absoluteEnd(Int32) -> Int32](./mlxslice/absoluteend%28_%29.md)
  End index resolving negative values (e.g. for gather operations)
- [func absoluteStart(Int32) -> Int32](./mlxslice/absolutestart%28_%29.md)
  Start index resolving negative values (e.g. for gather operations)
- [func end(Int32) -> Int32](./mlxslice/end%28_%29.md)
  End index using numpy conventions.
- [func start(Int32) -> Int32](./mlxslice/start%28_%29.md)
  Start index using numpy conventions.
### Default Implementations
- [Equatable Implementations](./mlxslice/equatable-implementations.md)
- [MLXArrayIndex Implementations](./mlxslice/mlxarrayindex-implementations.md)

## Relationships

### Conforms To
- [MLXArrayIndex](./mlxarrayindex.md)
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxslice)*