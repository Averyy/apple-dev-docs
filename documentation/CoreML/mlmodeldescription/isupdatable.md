# isUpdatable

**Framework**: Core ML  
**Kind**: property

A Boolean value that indicates whether you can update the model with additional training.

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
var isUpdatable: Bool { get }
```

## See Also

- [var trainingInputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/traininginputdescriptionsbyname.md)
  A dictionary of the training input feature descriptions, which the model keys by the input’s name.
- [var parameterDescriptionsByKey: [MLParameterKey : MLParameterDescription]](mlmodeldescription/parameterdescriptionsbykey.md)
  A dictionary of the descriptions for the model’s parameters.
- [class MLParameterDescription](mlparameterdescription.md)
  A description of a model parameter that includes a default value and a constraint, if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodeldescription/isupdatable)*