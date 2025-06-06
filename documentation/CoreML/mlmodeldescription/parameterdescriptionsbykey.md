# parameterDescriptionsByKey

**Framework**: Core ML  
**Kind**: property

A dictionary of the descriptions for the model’s parameters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var parameterDescriptionsByKey: [MLParameterKey : MLParameterDescription] { get }
```

## See Also

- [var isUpdatable: Bool](mlmodeldescription/isupdatable.md)
  A Boolean value that indicates whether you can update the model with additional training.
- [var trainingInputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/traininginputdescriptionsbyname.md)
  A dictionary of the training input feature descriptions, which the model keys by the input’s name.
- [class MLParameterDescription](mlparameterdescription.md)
  A description of a model parameter that includes a default value and a constraint, if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodeldescription/parameterdescriptionsbykey)*