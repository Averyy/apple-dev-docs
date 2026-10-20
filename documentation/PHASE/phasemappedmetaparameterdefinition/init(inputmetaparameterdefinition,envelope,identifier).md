# init(inputMetaParameterDefinition:envelope:identifier:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a specification for a named metaparameter that the app plots on a graph defined by the given set of curves.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(inputMetaParameterDefinition: PHASENumberMetaParameterDefinition, envelope: PHASEEnvelope, identifier: String)
```

```objc
- (instancetype) initWithInputMetaParameterDefinition:(PHASENumberMetaParameterDefinition *) inputMetaParameterDefinition envelope:(PHASEEnvelope *) envelope identifier:(NSString *) identifier;
```

## Parameters

- `inputMetaParameterDefinition`: A metaparameter that contains an input value.
- `envelope`: A set of curves that graph the input value.
- `identifier`: A unique name for the metaparameter specification.

## See Also

### Creating a Mapped Metaparameter
- [init(inputMetaParameterDefinition: PHASENumberMetaParameterDefinition, envelope: PHASEEnvelope)](./init%28inputmetaparameterdefinition,envelope%29.md)
  Creates a specification for a metaparameter that the app plots on a graph defined by the given set of curves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemappedmetaparameterdefinition/init(inputmetaparameterdefinition:envelope:identifier:))*