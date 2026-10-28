# numberOfNeighbors

**Framework**: Core ML  
**Kind**: property  
**Role**: Type Property

The key you use to access the number of neighbors that adjusts the affinity of a k-nearest-neighbor model.

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
class var numberOfNeighbors: MLParameterKey { get }
```

```objc
@property (class, nonatomic, readonly) MLParameterKey * numberOfNeighbors;
```

## Discussion

The value type for the [`numberOfNeighbors`](./numberofneighbors.md) key is an [`Int64`](../../Swift/int64.md).

## See Also

### Accessing model parameters
- [class var linkedModelFileName: MLParameterKey](./linkedmodelfilename.md)
  The key you use to access the linked model’s filename.
- [class var linkedModelSearchPath: MLParameterKey](./linkedmodelsearchpath.md)
  The key you use to access the linked model’s search path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlparameterkey/numberofneighbors)*