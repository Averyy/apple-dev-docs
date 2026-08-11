# init(operationCategory:requestedEvaluations:)

**Framework**: Trust Insights  
**Kind**: init

Creates the context with which to request insights.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
init(operationCategory: InsightEvaluator.OperationCategory, requestedEvaluations: (repeat each InsightRequest))
```

## Parameters

- `operationCategory`: For use in transparency logs and may affect insight results if data suggests it may be appropriate
- `requestedEvaluations`: Insights types and versions to request. These should all be of type InsightRequest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/insightcontext/init(operationcategory:requestedevaluations:))*