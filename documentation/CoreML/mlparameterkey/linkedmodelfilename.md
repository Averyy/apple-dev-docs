# linkedModelFileName

**Framework**: Core ML  
**Kind**: property  
**Role**: Type Property

The key you use to access the linked model’s filename.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class var linkedModelFileName: MLParameterKey { get }
```

```objc
@property (class, nonatomic, readonly) MLParameterKey * linkedModelFileName;
```

## Discussion

The value type for the [`linkedModelFileName`](./linkedmodelfilename.md) key is a [`String`](../../Swift/string.md).

## See Also

### Accessing model parameters
- [class var numberOfNeighbors: MLParameterKey](./numberofneighbors.md)
  The key you use to access the number of neighbors that adjusts the affinity of a k-nearest-neighbor model.
- [class var linkedModelSearchPath: MLParameterKey](./linkedmodelsearchpath.md)
  The key you use to access the linked model’s search path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlparameterkey/linkedmodelfilename)*