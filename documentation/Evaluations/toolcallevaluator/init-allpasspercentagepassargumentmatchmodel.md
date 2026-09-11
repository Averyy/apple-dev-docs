# init(allPass:percentagePass:argumentMatchModel:)

**Framework**: Evaluations  
**Kind**: init

Creates a new tool-call expectations evaluator with a custom language model for semantic matching of natural language argument matchers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
init(allPass: Metric, percentagePass: Metric, argumentMatchModel: any LanguageModel)
```

#### Discussion

```swift
let allPassMetric = Metric("Tools All Pass")
let percentagePassMetric = Metric("Tools Percentage Pass")

let evaluator = ToolCallEvaluator<ModelSample<String>>(
    allPass: allPassMetric,
    percentagePass: percentagePassMetric,
    argumentMatchModel: SystemLanguageModel.default
)
```

## Parameters

- `allPass`: The metric for the strict pass or fail result.
- `percentagePass`: The metric for the partial score result.
- `argumentMatchModel`: The language model to use for semantic matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolcallevaluator/init(allpass:percentagepass:argumentmatchmodel:))*