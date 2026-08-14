# IsLikelyBeingCoachedInsight

**Framework**: Trust Insights  
**Kind**: struct

An insight to request to examine indications that someone may be actively coaching a person to perform actions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct IsLikelyBeingCoachedInsight
```

#### Discussion

It could be useful to consider this in operations where it’s possible that someone may be in the process of being defrauded (such as transfers to new counterparties) and whether additional security checks — often called “step ups” or “blocks” — may be appropriate.

> **Note**: It’s important to be aware that coaching may not necessarily be malicious.

## Topics

### Instance Properties - generated
- [var insightID: String](islikelybeingcoachedinsight/insightid.md)
  The identifier for this particular result.
- [var modelVersion: String?](islikelybeingcoachedinsight/modelversion.md)
  The model version used for this particular insight.
- [var newestModelVersion: String?](islikelybeingcoachedinsight/newestmodelversion.md)
  The newest model that could be requested.
- [let outcome: Result<IsLikelyBeingCoachedInsight.Value, InsightError>](islikelybeingcoachedinsight/outcome.md)
  Result value from a request for this insight.
### Enumerations - generated
- [IsLikelyBeingCoachedInsight.SchemaVersion](islikelybeingcoachedinsight/schemaversion.md)
  An enumeration of insight values present in the available schema versions.
- [IsLikelyBeingCoachedInsight.Value](islikelybeingcoachedinsight/value.md)
  The levels of trust the framework returns for the “is likely being coached” insight.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [TrustInsight](trustinsight.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/islikelybeingcoachedinsight)*