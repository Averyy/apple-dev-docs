# parameters

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A dictionary of configuration settings your app can override when loading a model.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var parameters: [MLParameterKey : Any]? { get set }
```

```objc
@property (nonatomic, readwrite, nullable) NSDictionary<MLParameterKey *,id> * parameters;
```

## See Also

### Configuring model parameters
- [var functionName: String?](./functionname.md)
  Function name that `MLModel` will use.
- [var modelDisplayName: String?](./modeldisplayname.md)
  A human readable name of a model for display purposes.
- [class MLParameterKey](../mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelconfiguration/parameters)*