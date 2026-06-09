# operationCategory

**Framework**: TrustInsights  
**Kind**: property

The type of operation you’re requesting the evaluation for.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var operationCategory: InsightEvaluator.OperationCategory
```

#### Discussion

The framework may present information based on this request in the transparency log that shows the use of this framework by your app.

## See Also

- [var requestID: String?](insightevaluator/insightcontext/requestid.md)
  An optional identifier you can use to tie an assessment to a specific transaction.
- [let requestedInsight: (repeat each InsightRequest)](insightevaluator/insightcontext/requestedinsight.md)
  The insight you’re requesting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/insightcontext/operationcategory)*