# init(inputMetaParameterDefinition:envelope:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a specification for a metaparameter that the app plots on a graph defined by the given set of curves.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(inputMetaParameterDefinition: PHASENumberMetaParameterDefinition, envelope: PHASEEnvelope)
```

```objc
- (instancetype) initWithInputMetaParameterDefinition:(PHASENumberMetaParameterDefinition *) inputMetaParameterDefinition envelope:(PHASEEnvelope *) envelope;
```

## Parameters

- `inputMetaParameterDefinition`: A metaparameter that contains an input value.
- `envelope`: A set of curves that graph the input value.

## See Also

### Creating a Mapped Metaparameter
- [convenience init(inputMetaParameterDefinition: PHASENumberMetaParameterDefinition, envelope: PHASEEnvelope, identifier: String)](./init%28inputmetaparameterdefinition,envelope,identifier%29.md)
  Creates a specification for a named metaparameter that the app plots on a graph defined by the given set of curves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemappedmetaparameterdefinition/init(inputmetaparameterdefinition:envelope:))*