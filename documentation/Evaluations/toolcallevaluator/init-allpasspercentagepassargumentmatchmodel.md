# init(allPass:percentagePass:argumentMatchModel:)

**Framework**: Evaluations  
**Kind**: init

Creates a new tool-call expectations evaluator with a custom language model for semantic matching of natural language argument matchers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

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