# MLComputePlan.Cost

**Framework**: Core ML  
**Kind**: struct

A struct containing information on the estimated cost of executing a layer/operation.

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
struct Cost
```

## Topics

### Accessing the weight
- [let weight: Double](mlcomputeplan-1w21n/cost/weight.md)
  The estimated workload of executing the operation over the total model evaluation. The value is between [0.0, 1.0].

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func estimatedCost(of: MLModelStructure.Program.Operation) -> MLComputePlan.Cost?](mlcomputeplan-1w21n/estimatedcost(of:).md)
  Returns the estimated cost of executing a MLProgram operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-1w21n/cost)*