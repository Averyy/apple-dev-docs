---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nodenamer"
framework: "mlx-swift/MLX"
---

# NodeNamer

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

Assigns human readable names to arrays in a compute graph.

## Declaration

```swift
final class NodeNamer
```

## Overview

Arrays that aren’t given a name are numbered automatically.  Pass a namer to [`exportToDot(_:namer:)`](./exporttodot%28_,namer%29.md) or [`graphDescription(_:namer:)`](./graphdescription%28_,namer%29.md) to make their output easier to read:

```swift
let x = MLXArray([1, 2, 3])
let y = MLXArray([4, 5, 6])

let namer = NodeNamer()
namer.setName("x", for: x)
namer.setName("y", for: y)

print(exportToDot([x + y], namer: namer))
```

### See Also

- [`exportToDot(_:namer:)`](./exporttodot%28_,namer%29.md)
- [`graphDescription(_:namer:)`](./graphdescription%28_,namer%29.md)

## Topics

### Initializers
- [init()](./nodenamer/init%28%29.md)
  Create an empty namer.
### Instance Methods
- [func name(for: MLXArray) -> String?](./nodenamer/name%28for%29.md)
  The name of `array`.
- [func setName(String, for: MLXArray)](./nodenamer/setname%28_,for%29.md)
  Assign `name` to `array`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nodenamer)*