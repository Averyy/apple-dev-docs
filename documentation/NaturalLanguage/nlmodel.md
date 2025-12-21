# NLModel

**Framework**: Natural Language  
**Kind**: class

A custom model trained to classify or tag natural language text.

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
class NLModel
```

#### Overview

With [`Natural Language`](NaturalLanguage.md), you can create text classifier ([`MLTextClassifier`](https://developer.apple.com/documentation/CreateML/MLTextClassifier)) or word tagger ([`MLWordTagger`](https://developer.apple.com/documentation/CreateML/MLWordTagger)) models. Use [`NLModel`](nlmodel.md) to integrate those models into your app. This integration ensures that your tokenization and tagger configurations are identical when you train your model and use it in your app.

If you create a text classifier as described in doc:creating-a-text-classifier-model, you can integrate that model into your app and use it to make predictions like this:

```swift
let text = "I am very happy."

do {
    let mlModel = try SentimentClassifier(configuration: MLModelConfiguration()).model
        
    let customModel = try NLModel(mlModel: mlModel)
    
    // Use the text classifier model to get the most likely label.
    if let label = customModel.predictedLabel(for: text) {
        print("Most likely label: \(label)")
    }
    
    // Get multiple possible labels with their associated confidence scores.
    let labelHypotheses = customModel.predictedLabelHypotheses(for: text, maximumCount: 3)
    print("Label confidence scores: \(labelHypotheses)")
    
} catch {
    print(error)
}
```

If you create a custom word tagger as described in doc:creating-a-word-tagger-model, you can integrate that model into your app and generate tags for new text input like this:

```swift
let text = "The iPad is my favorite Apple product."

do {
    let mlModel = try AppleTagger(configuration: MLModelConfiguration()).model
        
    let customModel = try NLModel(mlModel: mlModel)
    let customTagScheme = NLTagScheme("Apple")
    
    let tagger = NLTagger(tagSchemes: [.nameType, customTagScheme])
    tagger.string = text
    tagger.setModels([customModel], forTagScheme: customTagScheme)
    
    tagger.enumerateTags(in: text.startIndex..<text.endIndex, unit: .word, 
                         scheme: customTagScheme, options: .omitWhitespace) { tag, tokenRange  in
        if let tag = tag {
            print("\(text[tokenRange]): \(tag.rawValue)")
        }
        return true
    }
} catch {
    print(error)
}
```

## Topics

### Creating a model
- [convenience init(mlModel: MLModel) throws](nlmodel/init(mlmodel:).md)
  Creates a new natural language model based on the given Core ML model instance.
- [convenience init(contentsOf: URL) throws](nlmodel/init(contentsof:).md)
  Creates a new natural language model based on a compiled Core ML model at the given URL.
### Making predictions
- [func predictedLabel(for: String) -> String?](nlmodel/predictedlabel(for:).md)
  Predicts a label for the given input string.
- [func predictedLabels(forTokens: [String]) -> [String]](nlmodel/predictedlabels(fortokens:).md)
  Predicts a label for each string in the given array.
- [func predictedLabelHypotheses(for: String, maximumCount: Int) -> [String : Double]](nlmodel/predictedlabelhypotheses(for:maximumcount:).md)
  Predicts multiple possible labels for the given input string.
- [func predictedLabelHypotheses(forTokens: [String], maximumCount: Int) -> [[String : Double]]](nlmodel/predictedlabelhypotheses(fortokens:maximumcount:).md)
  Predicts multiple possible labels for each string in the given array.
### Inspecting a model
- [var configuration: NLModelConfiguration](nlmodel/configuration.md)
  A configuration describing the natural language model.
- [class NLModelConfiguration](nlmodelconfiguration.md)
  The configuration parameters of a natural language model.
### Related Documentation
- [struct MLTextClassifier](../CreateML/MLTextClassifier.md)
  A model you train to classify natural language text.
- [struct MLWordTagger](../CreateML/MLWordTagger.md)
  A word-tagging model you train to classify natural language text at the word level.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating a text classifier model](../CreateML/creating-a-text-classifier-model.md)
  Train a machine learning model to classify natural language text.
- [Creating a word tagger model](../CreateML/creating-a-word-tagger-model.md)
  Train a machine learning model to tag individual words in natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlmodel)*