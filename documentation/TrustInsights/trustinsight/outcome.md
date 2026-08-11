# outcome

**Framework**: Trust Insights  
**Kind**: property  
**Required**: Yes

The result value from a request for this insight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
var outcome: Result<Self.Value, InsightError> { get }
```

## See Also

- [var insightID: String](trustinsight/insightid.md)
  The insight ID.
- [var isUsingCurrentModel: Bool](trustinsight/isusingcurrentmodel.md)
  A Boolean value that indicates whether the framework created the insight with the newest available model version.
- [var modelVersion: String?](trustinsight/modelversion.md)
  The model version the framework used for this insight.
- [var newestModelVersion: String?](trustinsight/newestmodelversion.md)
  The newest model that’s available to request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/trustinsight/outcome)*