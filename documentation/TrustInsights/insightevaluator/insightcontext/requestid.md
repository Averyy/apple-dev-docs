# requestID

**Framework**: Trust Insights  
**Kind**: property  
**Role**: Instance Property

An optional identifier you can use to tie an assessment to a specific transaction.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
var requestID: String?
```

## Discussion

It’s a best practice to use a server generated identifier and then to verify that your app includes it in the evaluation result. The enables your app to verify that the service produced the result in response to the specific request.

## See Also

### insight context properties
- [var operationCategory: InsightEvaluator.OperationCategory](./operationcategory.md)
  The type of operation you’re requesting the evaluation for.
- [let requestedInsight: (repeat each InsightRequest)](./requestedinsight.md)
  The insight you’re requesting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/insightcontext/requestid)*