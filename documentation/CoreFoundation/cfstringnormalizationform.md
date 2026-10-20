# CFStringNormalizationForm

**Framework**: Core Foundation  
**Kind**: enum  
**Role**: Enumeration

Unicode normalization forms as described in Unicode Technical Report #15.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CFStringNormalizationForm
```

```c
enum CFStringNormalizationForm : CFIndex;
```

## Topics

### Constants
- [CFStringNormalizationForm.D](./cfstringnormalizationform/d.md)
  Canonical decomposition.
- [CFStringNormalizationForm.KD](./cfstringnormalizationform/kd.md)
  Compatibility decomposition.
- [CFStringNormalizationForm.C](./cfstringnormalizationform/c.md)
  Canonical decomposition followed by canonical composition.
- [CFStringNormalizationForm.KC](./cfstringnormalizationform/kc.md)
  Compatibility decomposition followed by canonical composition.
### Initializers
- [init?(rawValue: CFIndex)](./cfstringnormalizationform/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [Transform Identifiers for CFStringTransform](./transform-identifiers-for-cfstringtransform.md)
  Constants that identify transforms used with [`CFStringTransform(_:_:_:_:)`](./cfstringtransform%28_,_,_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringnormalizationform)*