# modelDisplayName

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A human readable name of a model for display purposes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var modelDisplayName: String? { get set }
```

```objc
@property (copy, readwrite, nullable) NSString * modelDisplayName;
```

## See Also

### Configuring model parameters
- [var functionName: String?](./functionname.md)
  Function name that `MLModel` will use.
- [var parameters: [MLParameterKey : Any]?](./parameters.md)
  A dictionary of configuration settings your app can override when loading a model.
- [class MLParameterKey](../mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelconfiguration/modeldisplayname)*