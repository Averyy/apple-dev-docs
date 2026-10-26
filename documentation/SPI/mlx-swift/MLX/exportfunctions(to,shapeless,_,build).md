---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/exportfunctions(to:shapeless:_:build:)"
framework: "mlx-swift/MLX"
---

# exportFunctions(to:shapeless:_:build:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Export multiple traces of a function to a `.mlxfn` file.

## Declaration

```swift
func exportFunctions(to url: URL, shapeless: Bool = false, _ f: @escaping ([MLXArray]) -> [MLXArray], build: (FunctionExporterMultiple) throws -> Void) throws
```

#### Discussion

For example this defines a function, writes it to a file, imports it and evaluates it.

```swift
func f(_ arrays: [MLXArray]) -> [MLXArray] {
    [arrays.dropFirst().reduce(arrays[0], +)]
}

let x = MLXArray(1)

try exportFunctions(to: url, shapeless: true, f) { export in
    try export(x)
    try export(x, x)
    try export(x, x, x)
}

// load it back in
let f2 = try importFunction(from: url)

let a = MLXArray([10, 10, 10])
let b = MLXArray([5, 10, 20])
let c = MLXArray([1, 2, 3])

// r1 = a
let r1 = try f2(a)[0]

// r2 = a + b
let r2 = try f2(a, b)[0]

// r3 = a + b + c
let r3 = try f2(a, b, c)[0]
```

##### See Also

- [`exportFunction(to:shapeless:_:)`](./exportfunction%28to,shapeless,_%29.md)
- [`importFunction(from:)`](./importfunction%28from%29.md)

## Parameters

- `url`: File url to write the `.mlxfn` file
- `shapeless`: If `true` the function allows inputs with variable shapes
- `f`: The function to capture
- `build`: Closure for recording the calls


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/exportfunctions(to:shapeless:_:build:))*