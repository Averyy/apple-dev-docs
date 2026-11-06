# computeSiriMetrics(into:)

**Framework**: Evaluations  
**Kind**: method  
**Role**: Type Method

The report’s summary cards: one per question, grouped into sections, each the share of scenarios where it held.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- Xcode 27.0+

## Declaration

```swift
static func computeSiriMetrics(into aggregator: inout MetricsAggregator)
```

Available when `Subject` is `SiriScenarioSubject`.

## Discussion

Call it from `aggregateMetrics(using:)` to keep the standard report, e.g. before adding cards of your own.

Xcode titles a card per group, and the grouping is the only ordering the report honours — the cards themselves come back from an unordered dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluation/computesirimetrics(into:))*