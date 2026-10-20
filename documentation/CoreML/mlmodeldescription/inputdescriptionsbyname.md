# inputDescriptionsByName

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A dictionary of input feature descriptions, which the model keys by the input’s name.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var inputDescriptionsByName: [String : MLFeatureDescription] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,MLFeatureDescription *> * inputDescriptionsByName;
```

## See Also

### Accessing feature descriptions
- [var stateDescriptionsByName: [String : MLFeatureDescription]](./statedescriptionsbyname.md)
  Description of the state features.
- [var outputDescriptionsByName: [String : MLFeatureDescription]](./outputdescriptionsbyname.md)
  A dictionary of output feature descriptions, which the model keys by the output’s name.
- [class MLFeatureDescription](../mlfeaturedescription.md)
  The name, type, and constraints of an input or output feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodeldescription/inputdescriptionsbyname)*