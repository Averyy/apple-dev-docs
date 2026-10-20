# language

**Framework**: Natural Language  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NLLanguage language;
```

## See Also

### Accessing the configuration
- [var revision: Int](./revision.md)
  The version of the Natural Language framework that trained the model.
- [class func supportedRevisions(for: NLModel.ModelType) -> IndexSet](./supportedrevisions%28for%29.md)
  Returns the versions of the Natural Language framework the OS supports.
- [class func currentRevision(for: NLModel.ModelType) -> Int](./currentrevision%28for%29.md)
  Returns the current Natural Language framework version in the OS.
- [var type: NLModel.ModelType](./type.md)
  The natural language model type of the model.
- [NLModel.ModelType](../nlmodel/modeltype.md)
  The different types of a natural language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodelconfiguration/language)*