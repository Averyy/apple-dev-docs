# modelVersion

**Framework**: Trust Insights  
**Kind**: property  
**Required**: Yes

The model version the framework used for this insight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var modelVersion: String? { get }
```

## See Also

- [var insightID: String](trustinsight/insightid.md)
  The insight ID.
- [var isUsingCurrentModel: Bool](trustinsight/isusingcurrentmodel.md)
  A Boolean value that indicates whether the framework created the insight with the newest available model version.
- [var newestModelVersion: String?](trustinsight/newestmodelversion.md)
  The newest model that’s available to request.
- [var outcome: Result<Self.Value, InsightError>](trustinsight/outcome.md)
  The result value from a request for this insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/trustinsight/modelversion)*