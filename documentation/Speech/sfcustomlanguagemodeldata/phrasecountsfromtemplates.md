# SFCustomLanguageModelData.PhraseCountsFromTemplates

**Framework**: Speech  
**Kind**: struct  
**Role**: Structure

A type that can be used to construct custom language model data by specifying a set of template classes and using the result builder DSL to specify templates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+

## Declaration

```swift
struct PhraseCountsFromTemplates
```

## Topics

### Creating weighted phrases from templates
- [init(classes: [String : [String]], builder: () -> any TemplateInsertable)](./phrasecountsfromtemplates/init%28classes,builder%29.md)

## Relationships

### Conforms To
- [DataInsertable](../datainsertable.md)

## See Also

### Adding parameterized sample data within a result builder
- [SFCustomLanguageModelData.TemplateInsertableBuilder](./templateinsertablebuilder.md)
  A custom parameter attribute that constructs custom language model data from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/phrasecountsfromtemplates)*