# estimatedCost(of:)

**Framework**: Core ML  
**Kind**: method

Returns the estimated cost of executing a MLProgram operation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
func estimatedCost(of operation: MLModelStructure.Program.Operation) -> MLComputePlan.Cost?
```

#### Return Value

The estimated cost of executing the operation.

## Parameters

- `operation`: A MLProgram operation

## See Also

- [MLComputePlan.Cost](mlcomputeplan-1w21n/cost.md)
  A struct containing information on the estimated cost of executing a layer/operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-1w21n/estimatedcost(of:))*