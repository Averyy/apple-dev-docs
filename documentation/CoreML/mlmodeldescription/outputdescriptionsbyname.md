# outputDescriptionsByName

**Framework**: Core ML  
**Kind**: property

A dictionary of output feature descriptions, which the model keys by the output’s name.

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
var outputDescriptionsByName: [String : MLFeatureDescription] { get }
```

## See Also

- [var inputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/inputdescriptionsbyname.md)
  A dictionary of input feature descriptions, which the model keys by the input’s name.
- [class MLFeatureDescription](mlfeaturedescription.md)
  The name, type, and constraints of an input or output feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodeldescription/outputdescriptionsbyname)*