# gainMetaParameterDefinition

**Framework**: PHASE  
**Kind**: property

A template for a parameter that changes the mixer’s volume gradually over a period of time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var gainMetaParameterDefinition: PHASENumberMetaParameterDefinition? { get set }
```

#### Discussion

When the framework creates a mixer from a mixer definition, PHASE initializes the mixer’s [`gainMetaParameter`](phasepushstreamnode/gainmetaparameter.md) to this property’s values.

## See Also

- [var gain: Double](phasemixerdefinition/gain.md)
  The mixer’s volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemixerdefinition/gainmetaparameterdefinition)*