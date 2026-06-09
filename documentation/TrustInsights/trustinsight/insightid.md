# insightID

**Framework**: TrustInsights  
**Kind**: property  
**Required**: Yes

The insight ID.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var insightID: String { get }
```

## See Also

- [var isUsingCurrentModel: Bool](trustinsight/isusingcurrentmodel.md)
  A Boolean value that indicates whether the framework created the insight with the newest available model version.
- [var modelVersion: String?](trustinsight/modelversion.md)
  The model version the framework used for this insight.
- [var newestModelVersion: String?](trustinsight/newestmodelversion.md)
  The newest model that’s available to request.
- [var outcome: Result<Self.Value, InsightError>](trustinsight/outcome.md)
  The result value from a request for this insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/trustinsight/insightid)*