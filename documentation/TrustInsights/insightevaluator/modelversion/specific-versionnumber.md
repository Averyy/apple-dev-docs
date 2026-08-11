# InsightEvaluator.ModelVersion.specific(versionNumber:)

**Framework**: Trust Insights  
**Kind**: case

A value that defines a specific model version intended to be run in parallel with the latest version.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
case specific(versionNumber: String)
```

#### Discussion

You can use this to enable validation of or update your your internal server-side risk model to adapt to changes to weights that incorporate this insight.

## See Also

- [InsightEvaluator.ModelVersion.current](insightevaluator/modelversion/current.md)
  A value that defines the latest version and includes adjustments as fraud patterns change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/insightevaluator/modelversion/specific(versionnumber:))*