# withMLTensorComputePolicy(_:_:)

**Framework**: Core ML  
**Kind**: func

Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func withMLTensorComputePolicy<Result>(_ computePolicy: MLComputePolicy, _ body: () throws -> Result) rethrows -> Result
```

#### Return Value

The return value, if any, of the `body` closure.

## Parameters

- `computePolicy`: A compute policy that will be set before the closure gets called and restored after the closure returns.
- `body`: A nullary closure. If the closure has a return value, that value is also used as the return value of the    function.

## See Also

- [class MLComputePlan](mlcomputeplan-1w21n.md)
  A class representing the compute plan of a model.
- [enum MLModelStructure](mlmodelstructure-swift.enum.md)
  An enum representing the structure of a model.
- [struct MLComputePolicy](mlcomputepolicy.md)
  The compute policy determining what compute device, or compute devices, to execute ML workloads on.
- [func withMLTensorComputePolicy<R>(MLComputePolicy, () async throws -> R) async rethrows -> R](withmltensorcomputepolicy(_:_:)-8stx9.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/withmltensorcomputepolicy(_:_:)-6z33x)*