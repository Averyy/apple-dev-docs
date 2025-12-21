# functionName

**Framework**: Core ML  
**Kind**: property

Function name that `MLModel` will use.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var functionName: String? { get set }
```

#### Discussion

Some model types (e.g. ML Program) supports multiple functions in a model asset, where each `MLModel` instance is associated with a particular function.

Use `MLModelAsset` to get the list of available functions. Use `nil` to use a default function.

```swift
let configuration = MLModelConfiguration()
configuration.functionName = "my_function"
```

## See Also

- [var modelDisplayName: String?](mlmodelconfiguration/modeldisplayname.md)
  A human readable name of a model for display purposes.
- [var parameters: [MLParameterKey : Any]?](mlmodelconfiguration/parameters.md)
  A dictionary of configuration settings your app can override when loading a model.
- [class MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelconfiguration/functionname)*