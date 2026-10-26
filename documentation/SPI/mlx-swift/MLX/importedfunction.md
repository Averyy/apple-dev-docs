---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/importedfunction"
framework: "mlx-swift/MLX"
---

# ImportedFunction

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

Helper for [`importFunction(from:)`](./importfunction%28from%29.md) – this holds the imported function.

## Declaration

```swift
@dynamicCallable
final class ImportedFunction
```

#### Overview

This can be called with parameters that match the recorded parameters:

```swift
func f(arrays: [MLXArray]) -> [MLXArray] {
    [arrays[0] * arrays[1]]
}

let x = MLXArray(1)
let y = MLXArray([1, 2, 3])

// records with unnamed first parameter and a second parameter named `y`
try exportFunction(to: url, f)(x, y: y)

// f2 is a ImportedFunction
let f2 = try importFunction(from: url)

let a = MLXArray(10)
let b = MLXArray([5, 10, 20])

// call it -- the shapes and labels have to match
let r = try f2(a, y: b)[0]
```

## Topics

### Initializers
- [init(url: URL) throws](./importedfunction/init%28url%29.md)
### Instance Methods
- [func dynamicallyCall(withKeywordArguments: KeyValuePairs<String, MLXArray>) throws -> [MLXArray]](./importedfunction/dynamicallycall%28withkeywordarguments%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/importedfunction)*