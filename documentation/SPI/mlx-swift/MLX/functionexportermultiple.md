---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/functionexportermultiple"
framework: "mlx-swift/MLX"
---

# FunctionExporterMultiple

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

A helper for [`exportFunctions(to:shapeless:_:build:)`](./exportfunctions%28to,shapeless,_,build%29.md).

## Declaration

```swift
@dynamicCallable
final class FunctionExporterMultiple
```

## Overview

This records the call to the function and saves it to the file.

```swift
func f(_ arrays: [MLXArray]) -> [MLXArray] {
    [arrays.dropFirst().reduce(arrays[0], +)]
}

let x = MLXArray(1)

// the export parameter is a FunctionExporterMultiple
try exportFunctions(to: url, shapeless: true, f) { export in
    try export(x)
    try export(x, x)
    try export(x, x, x)
}
```

### See Also

- [`exportFunctions(to:shapeless:_:build:)`](./exportfunctions%28to,shapeless,_,build%29.md)

## Topics

### Instance Methods
- [func dynamicallyCall(withKeywordArguments: KeyValuePairs<String, MLXArray>) throws](./functionexportermultiple/dynamicallycall%28withkeywordarguments%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/functionexportermultiple)*