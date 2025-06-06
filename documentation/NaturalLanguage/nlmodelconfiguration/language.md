# language

**Framework**: Natural Language  
**Kind**: property

The language the model supports.

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
var language: NLLanguage? { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodelconfiguration/language)*