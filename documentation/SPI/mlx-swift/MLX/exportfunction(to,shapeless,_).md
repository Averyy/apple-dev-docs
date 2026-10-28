---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/exportfunction(to:shapeless:_:)"
framework: "mlx-swift/MLX"
---

# exportFunction(to:shapeless:_:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Export a function to a `.mlxfn` file.

## Declaration

```swift
func exportFunction(to url: URL, shapeless: Bool = false, _ f: @escaping ([MLXArray]) -> [MLXArray]) -> FunctionExporterSingle
```

## Return Value

A helper ([`FunctionExporterSingle`](./functionexportersingle.md)) that records the call

## Discussion

For example this defines a function, writes it to a file, imports it and evaluates it.

```swift
func f(arrays: [MLXArray]) -> [MLXArray] {
    [arrays[0] * arrays[1]]
}

let x = MLXArray(1)
let y = MLXArray([1, 2, 3])

try exportFunction(to: url, f)(x, y: y)

// load it back in
let f2 = try importFunction(from: url)

let a = MLXArray(10)
let b = MLXArray([5, 10, 20])

// call it -- the shapes and labels have to match
let r = try f2(a, y: b)[0]
```

### See Also

- [`exportFunctions(to:shapeless:_:build:)`](./exportfunctions%28to,shapeless,_,build%29.md)
- [`importFunction(from:)`](./importfunction%28from%29.md)

## Parameters

- `url`: File url to write the `.mlxfn` file
- `shapeless`: If `true` the function allows inputs with variable shapes
- `f`: The function to capture


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/exportfunction(to:shapeless:_:))*