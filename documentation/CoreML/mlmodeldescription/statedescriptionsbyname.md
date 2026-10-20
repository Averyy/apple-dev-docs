# stateDescriptionsByName

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

Description of the state features.

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
var stateDescriptionsByName: [String : MLFeatureDescription] { get }
```

```objc
@property (nonatomic, readonly) NSDictionary<NSString *,MLFeatureDescription *> * stateDescriptionsByName;
```

## See Also

### Accessing feature descriptions
- [var inputDescriptionsByName: [String : MLFeatureDescription]](./inputdescriptionsbyname.md)
  A dictionary of input feature descriptions, which the model keys by the input’s name.
- [var outputDescriptionsByName: [String : MLFeatureDescription]](./outputdescriptionsbyname.md)
  A dictionary of output feature descriptions, which the model keys by the output’s name.
- [class MLFeatureDescription](../mlfeaturedescription.md)
  The name, type, and constraints of an input or output feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodeldescription/statedescriptionsbyname)*