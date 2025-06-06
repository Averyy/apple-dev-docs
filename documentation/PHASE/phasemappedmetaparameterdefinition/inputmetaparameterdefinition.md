# inputMetaParameterDefinition

**Framework**: PHASE  
**Kind**: property

A linear input value to plot on a curve.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var inputMetaParameterDefinition: PHASENumberMetaParameterDefinition { get }
```

#### Discussion

This property defines the input value to plot on a graph defined by [`envelope`](phasemappedmetaparameterdefinition/envelope.md).

To retrieve the output value, an app passes the metaparameter’s [`value`](phasemetaparameter/value.md) to the [`evaluate(x:)`](phaseenvelope/evaluate(x:).md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemappedmetaparameterdefinition/inputmetaparameterdefinition)*