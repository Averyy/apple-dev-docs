---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/importfunction(from:)"
framework: "mlx-swift/MLX"
---

# importFunction(from:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Imports a function from a `.mlxfn` file.

## Declaration

```swift
func importFunction(from url: URL) throws -> ImportedFunction
```

#### Return Value

A callable that represents the loaded function

#### Discussion

```swift
// f is a callable that represents the loaded function
let f = try importFunction(from: url)

let a = MLXArray(10)
let b = MLXArray([5, 10, 20])

// call it -- the shapes and labels have to match
let r = try f(a, y: b)[0]
```

##### See Also

- [`exportFunction(to:shapeless:_:)`](./exportfunction%28to,shapeless,_%29.md)
- [`exportFunctions(to:shapeless:_:build:)`](./exportfunctions%28to,shapeless,_,build%29.md)

## Parameters

- `url`: File to load from


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/importfunction(from:))*