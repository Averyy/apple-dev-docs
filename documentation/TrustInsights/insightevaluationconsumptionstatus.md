# InsightEvaluationConsumptionStatus

**Framework**: Trust Insights  
**Kind**: enum

Values describing the usage of insight evaluation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@nonexhaustive enum InsightEvaluationConsumptionStatus
```

## Topics

### Consumption status values
- [InsightEvaluationConsumptionStatus.notUsedError](insightevaluationconsumptionstatus/notusederror.md)
  A value that indicates the app couldn’t use the insights because of a technical failure, they arrived too late to be of use, or other issue.
- [InsightEvaluationConsumptionStatus.notUsedNotNeeded](insightevaluationconsumptionstatus/notusednotneeded.md)
  A value that indicates the app canceled the operation, so no decision required.
- [InsightEvaluationConsumptionStatus.usedEvaluationOnly](insightevaluationconsumptionstatus/usedevaluationonly.md)
  A value that indicates the app used the insights for evaluation of their usefulness or for model training with no impact on a decision process.
- [InsightEvaluationConsumptionStatus.usedIncreasedFriction](insightevaluationconsumptionstatus/usedincreasedfriction.md)
  A value that indicates the app evaluated the insights and they were a factor in adding checks or blocking the action.
- [InsightEvaluationConsumptionStatus.usedReducedFriction](insightevaluationconsumptionstatus/usedreducedfriction.md)
  A value that indicates the app evaluated the insights and they were a factor in making the operation easier for the user.
- [InsightEvaluationConsumptionStatus.usedUnchangedFriction](insightevaluationconsumptionstatus/usedunchangedfriction.md)
  A value that indicates the app evaluated the insights, but the insights didn’t have any impact on the decision or user flow.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum InsightError](insighterror.md)
  Error values the framework returns for specific insights within the overall evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluationconsumptionstatus)*