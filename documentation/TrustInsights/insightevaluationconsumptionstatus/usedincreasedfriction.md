# InsightEvaluationConsumptionStatus.usedIncreasedFriction

**Framework**: Trust Insights  
**Kind**: case  
**Role**: Case

A value that indicates the app evaluated the insights and they were a factor in adding checks or blocking the action.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
case usedIncreasedFriction
```

## See Also

### Consumption status values
- [InsightEvaluationConsumptionStatus.notUsedError](./notusederror.md)
  A value that indicates the app couldn’t use the insights because of a technical failure, they arrived too late to be of use, or other issue.
- [InsightEvaluationConsumptionStatus.notUsedNotNeeded](./notusednotneeded.md)
  A value that indicates the app canceled the operation, so no decision required.
- [InsightEvaluationConsumptionStatus.usedEvaluationOnly](./usedevaluationonly.md)
  A value that indicates the app used the insights for evaluation of their usefulness or for model training with no impact on a decision process.
- [InsightEvaluationConsumptionStatus.usedReducedFriction](./usedreducedfriction.md)
  A value that indicates the app evaluated the insights and they were a factor in making the operation easier for the user.
- [InsightEvaluationConsumptionStatus.usedUnchangedFriction](./usedunchangedfriction.md)
  A value that indicates the app evaluated the insights, but the insights didn’t have any impact on the decision or user flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluationconsumptionstatus/usedincreasedfriction)*