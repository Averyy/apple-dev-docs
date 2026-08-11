# isUsingCurrentModel

**Framework**: Trust Insights  
**Kind**: property

A Boolean value that indicates whether the framework created the insight with the newest available model version.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
var isUsingCurrentModel: Bool { get }
```

## See Also

- [var insightID: String](trustinsight/insightid.md)
  The insight ID.
- [var modelVersion: String?](trustinsight/modelversion.md)
  The model version the framework used for this insight.
- [var newestModelVersion: String?](trustinsight/newestmodelversion.md)
  The newest model that’s available to request.
- [var outcome: Result<Self.Value, InsightError>](trustinsight/outcome.md)
  The result value from a request for this insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/trustinsight/isusingcurrentmodel)*