# isUsingCurrentModel

**Framework**: Trust Insights  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the framework created the insight with the newest available model version.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
var isUsingCurrentModel: Bool { get }
```

## See Also

### Instance Properties - generated
- [var insightID: String](./insightid.md)
  The insight ID.
- [var modelVersion: String?](./modelversion.md)
  The model version the framework used for this insight.
- [var newestModelVersion: String?](./newestmodelversion.md)
  The newest model that’s available to request.
- [var outcome: Result<Self.Value, InsightError>](./outcome.md)
  The result value from a request for this insight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/trustinsight/isusingcurrentmodel)*