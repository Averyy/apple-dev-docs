# estimatedCostOfMLProgramOperation:

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns the estimated cost of executing an ML Program operation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```objc
- (MLComputePlanCost *) estimatedCostOfMLProgramOperation:(MLModelStructureProgramOperation *) operation;
```

#### Return Value

The estimated cost of executing the operation or nil if the cost couldn’t be estimated.

## Parameters

- `operation`: An ML Program operation.

## See Also

### Getting the estimated cost
- [MLComputePlanCost](../mlcomputeplancost.md)
  A class that represents the estimated cost of executing a layer or operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-85vdw/estimatedcostofmlprogramoperation:)*