# inputMetaParameterDefinition

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, readonly) PHASENumberMetaParameterDefinition * inputMetaParameterDefinition;
```

## Discussion

This property defines the input value to plot on a graph defined by [`envelope`](./envelope.md).

To retrieve the output value, an app passes the metaparameter’s [`value`](../phasemetaparameter/value.md) to the [`evaluate(x:)`](../phaseenvelope/evaluate%28x%29.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemappedmetaparameterdefinition/inputmetaparameterdefinition)*