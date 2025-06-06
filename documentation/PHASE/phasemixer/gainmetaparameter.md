# gainMetaParameter

**Framework**: PHASE  
**Kind**: property

A parameter that changes the mixer’s volume gradually over a period of time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var gainMetaParameter: PHASEMetaParameter? { get }
```

#### Discussion

Use this property to smoothly adjust the volume of the mixer’s audio signals by calling [`fade(value:duration:)`](phasenumbermetaparameter/fade(value:duration:).md).

The framework sets the initial value of this property according to the metaparameter definition object’s [`gainMetaParameterDefinition`](phasemixerdefinition/gainmetaparameterdefinition.md).

## See Also

- [var gain: Double](phasemixer/gain.md)
  The mixer’s volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemixer/gainmetaparameter)*