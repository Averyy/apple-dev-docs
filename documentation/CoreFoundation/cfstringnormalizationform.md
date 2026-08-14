# CFStringNormalizationForm

**Framework**: Core Foundation  
**Kind**: enum

Unicode normalization forms as described in Unicode Technical Report #15.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CFStringNormalizationForm
```

## Topics

### Constants
- [CFStringNormalizationForm.D](cfstringnormalizationform/d.md)
  Canonical decomposition.
- [CFStringNormalizationForm.KD](cfstringnormalizationform/kd.md)
  Compatibility decomposition.
- [CFStringNormalizationForm.C](cfstringnormalizationform/c.md)
  Canonical decomposition followed by canonical composition.
- [CFStringNormalizationForm.KC](cfstringnormalizationform/kc.md)
  Compatibility decomposition followed by canonical composition.
### Initializers
- [init?(rawValue: CFIndex)](cfstringnormalizationform/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Transform Identifiers for CFStringTransform](transform-identifiers-for-cfstringtransform.md)
  Constants that identify transforms used with [`CFStringTransform(_:_:_:_:)`](cfstringtransform(_:_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringnormalizationform)*