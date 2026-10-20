# init(switchMetaParameterDefinition:identifier:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a named node that invokes a child node based on the value of the given parameter.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(switchMetaParameterDefinition: PHASEStringMetaParameterDefinition, identifier: String)
```

```objc
- (instancetype) initWithSwitchMetaParameterDefinition:(PHASEStringMetaParameterDefinition *) switchMetaParameterDefinition identifier:(NSString *) identifier;
```

## Parameters

- `switchMetaParameterDefinition`: A string meta parameter that specifies the child node identifier to pass invocation on to.
- `identifier`: A unique name for the switch node.

## See Also

### Creating a Node
- [init(switchMetaParameterDefinition: PHASEStringMetaParameterDefinition)](./init%28switchmetaparameterdefinition%29.md)
  Creates a node that invokes a child node based on the value of the given parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseswitchnodedefinition/init(switchmetaparameterdefinition:identifier:))*