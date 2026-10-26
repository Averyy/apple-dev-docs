---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/functionexportersingle"
framework: "mlx-swift/MLX"
---

# FunctionExporterSingle

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

A helper for [`exportFunction(to:shapeless:_:)`](./exportfunction%28to,shapeless,_%29.md).

## Declaration

```swift
@dynamicCallable
final class FunctionExporterSingle
```

#### Overview

This records the call to the function and saves it to the file.

```swift
func f(arrays: [MLXArray]) -> [MLXArray] {
    [arrays[0] * arrays[1]]
}

let x = MLXArray(1)
let y = MLXArray([1, 2, 3])

// the (x, y: y) is calling this object
try exportFunction(to: url, f)(x, y: y)
```

##### See Also

- [`exportFunction(to:shapeless:_:)`](./exportfunction%28to,shapeless,_%29.md)

## Topics

### Instance Methods
- [func dynamicallyCall(withKeywordArguments: KeyValuePairs<String, MLXArray>) throws](./functionexportersingle/dynamicallycall%28withkeywordarguments%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/functionexportersingle)*