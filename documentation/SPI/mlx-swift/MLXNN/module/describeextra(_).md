---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/describeextra(_:)"
framework: "mlx-swift/MLXNN"
---

# describeExtra(_:)

**Framework**: mlx-swift/MLXNN  
**Kind**: method  
**Role**: Instance Method

Describe extra parameters.

## Declaration

```swift
func describeExtra(_ indent: Int) -> String
```

## Discussion

This will print a description of [`ModuleValue.other(_:)`](../modulevalue/other%28_%29.md) ivars, e.g.:

```swift
let eps: Float
```

Subclasses can override this to print custom information, e.g. shape information derived from parameters:

```swift
public override func describeExtra(_ indent: Int) -> String {
    "(inputDimensions=\(weight.dim(1)), outputDimensions=\(weight.dim(0)), bias=\(bias == nil ? "false" : /// "true"))"
}
```

### See Also

- [`description(indent:)`](./description%28indent%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/module/describeextra(_:))*