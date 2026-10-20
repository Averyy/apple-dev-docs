# init(switchMetaParameterDefinition:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a node that invokes a child node based on the value of the given parameter.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(switchMetaParameterDefinition: PHASEStringMetaParameterDefinition)
```

```objc
- (instancetype) initWithSwitchMetaParameterDefinition:(PHASEStringMetaParameterDefinition *) switchMetaParameterDefinition;
```

## Parameters

- `switchMetaParameterDefinition`: A string meta parameter that specifies the child node identifier to pass invocation on to.

## See Also

### Creating a Node
- [convenience init(switchMetaParameterDefinition: PHASEStringMetaParameterDefinition, identifier: String)](./init%28switchmetaparameterdefinition,identifier%29.md)
  Creates a named node that invokes a child node based on the value of the given parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseswitchnodedefinition/init(switchmetaparameterdefinition:))*