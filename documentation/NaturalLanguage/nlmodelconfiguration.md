# NLModelConfiguration

**Framework**: Natural Language  
**Kind**: class

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

## Topics

### Accessing the configuration
- [var language: NLLanguage?](nlmodelconfiguration/language.md)
  The language the model supports.
- [var revision: Int](nlmodelconfiguration/revision.md)
  The version of the Natural Language framework that trained the model.
- [class func supportedRevisions(for: NLModel.ModelType) -> IndexSet](nlmodelconfiguration/supportedrevisions(for:).md)
  Returns the versions of the Natural Language framework the OS supports.
- [class func currentRevision(for: NLModel.ModelType) -> Int](nlmodelconfiguration/currentrevision(for:).md)
  Returns the current Natural Language framework version in the OS.
- [var type: NLModel.ModelType](nlmodelconfiguration/type.md)
  The natural language model type of the model.
- [NLModel.ModelType](nlmodel/modeltype.md)
  The different types of a natural language model.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var configuration: NLModelConfiguration](nlmodel/configuration.md)
  A configuration describing the natural language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodelconfiguration)*