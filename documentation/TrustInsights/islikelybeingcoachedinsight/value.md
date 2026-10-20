# IsLikelyBeingCoachedInsight.Value

**Framework**: Trust Insights  
**Kind**: enum  
**Role**: Enumeration

The levels of trust the framework returns for the “is likely being coached” insight.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
@nonexhaustive enum Value
```

#### Discussion

The framework only returns additional result values when requesting a schema version that introduced a new value.

## Topics

### Enumeration Cases - generated
- [IsLikelyBeingCoachedInsight.Value.high](./value/high.md)
  A result that indicates there’s a high risk that a third party is coaching a person in some form.
- [IsLikelyBeingCoachedInsight.Value.medium](./value/medium.md)
  A result that indicates there’s a medium chance that a third party is coaching a person in some form.
- [IsLikelyBeingCoachedInsight.Value.unknown](./value/unknown.md)
  A result that indicates a lack of evidence as to whether or not coaching is occurring.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations - generated
- [IsLikelyBeingCoachedInsight.SchemaVersion](./schemaversion.md)
  An enumeration of insight values present in the available schema versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/trustinsights/islikelybeingcoachedinsight/value)*