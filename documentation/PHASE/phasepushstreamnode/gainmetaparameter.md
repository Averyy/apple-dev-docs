# gainMetaParameter

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A meta parameter for dynamic loudness control.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var gainMetaParameter: PHASENumberMetaParameter? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) PHASENumberMetaParameter * gainMetaParameter;
```

#### Discussion

The framework sets this property when the app specifies a meta parameter definition at initialization.

## See Also

### Controlling Playback
- [var rateMetaParameter: PHASENumberMetaParameter?](./ratemetaparameter.md)
  A meta parameter for dynamic rate control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepushstreamnode/gainmetaparameter)*