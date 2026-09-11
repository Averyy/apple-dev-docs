# init(allPass:percentagePass:)

**Framework**: Evaluations  
**Kind**: init

Creates a new tool-call expectations evaluator.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- Xcode 27.0+

## Declaration

```swift
init(allPass: Metric, percentagePass: Metric)
```

#### Discussion

The evaluator evaluates expectations once and produces two columns: a strict score (pass or fail) and a partial score (proportion matched).

```swift
let allPassMetric = Metric("Tools All Pass")
let percentagePassMetric = Metric("Tools Percentage Pass")

let evaluator = ToolCallEvaluator<ModelSample<String>>(
    allPass: allPassMetric,
    percentagePass: percentagePassMetric
)
```

## Parameters

- `allPass`: The metric for the strict pass or fail result.
- `percentagePass`: The metric for the partial score result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolcallevaluator/init(allpass:percentagepass:))*