# NLModelConfiguration

**Framework**: Natural Language  
**Kind**: class  
**Role**: Class

The configuration parameters of a natural language model.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class NLModelConfiguration
```

```objc
@interface NLModelConfiguration : NSObject
```

## Topics

### Accessing the configuration
- [var language: NLLanguage?](./nlmodelconfiguration/language.md)
  The language the model supports.
- [var revision: Int](./nlmodelconfiguration/revision.md)
  The version of the Natural Language framework that trained the model.
- [class func supportedRevisions(for: NLModel.ModelType) -> IndexSet](./nlmodelconfiguration/supportedrevisions%28for%29.md)
  Returns the versions of the Natural Language framework the OS supports.
- [class func currentRevision(for: NLModel.ModelType) -> Int](./nlmodelconfiguration/currentrevision%28for%29.md)
  Returns the current Natural Language framework version in the OS.
- [var type: NLModel.ModelType](./nlmodelconfiguration/type.md)
  The natural language model type of the model.
- [NLModel.ModelType](./nlmodel/modeltype.md)
  The different types of a natural language model.
### Initializers
- [init?(coder: NSCoder)](./nlmodelconfiguration/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Inspecting a model
- [var configuration: NLModelConfiguration](./nlmodel/configuration.md)
  A configuration describing the natural language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodelconfiguration)*