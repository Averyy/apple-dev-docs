# miniBatchIndex

**Framework**: Core ML  
**Kind**: property  
**Role**: Type Property

The key you use to access the mini-batch index (an `Int64` value) within an epoch.

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
class var miniBatchIndex: MLMetricKey { get }
```

```objc
@property (class, nonatomic, readonly) MLMetricKey * miniBatchIndex;
```

## Discussion

Use this key to fetch the mini-batch index value in the [`metrics`](../mlupdatecontext/metrics.md) dictionary.

## See Also

### Getting the keys
- [class var lossValue: MLMetricKey](./lossvalue.md)
  The key you use to access the current loss (a `float` value).
- [class var epochIndex: MLMetricKey](./epochindex.md)
  The key you use to access the epoch index (an `Int64` value).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmetrickey/minibatchindex)*