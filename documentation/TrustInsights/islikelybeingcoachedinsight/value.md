# IsLikelyBeingCoachedInsight.Value

**Framework**: Trust Insights  
**Kind**: enum

The levels of trust the framework returns for the “is likely being coached” insight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
@nonexhaustive enum Value
```

#### Discussion

The framework only returns additional result values when requesting a schema version that introduced a new value.

## Topics

### Enumeration Cases - generated
- [IsLikelyBeingCoachedInsight.Value.high](islikelybeingcoachedinsight/value/high.md)
  A result that indicates there’s a high risk that a third party is coaching a person in some form.
- [IsLikelyBeingCoachedInsight.Value.medium](islikelybeingcoachedinsight/value/medium.md)
  A result that indicates there’s a medium chance that a third party is coaching a person in some form.
- [IsLikelyBeingCoachedInsight.Value.unknown](islikelybeingcoachedinsight/value/unknown.md)
  A result that indicates a lack of evidence as to whether or not coaching is occurring.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [IsLikelyBeingCoachedInsight.SchemaVersion](islikelybeingcoachedinsight/schemaversion.md)
  An enumeration of insight values present in the available schema versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/islikelybeingcoachedinsight/value)*