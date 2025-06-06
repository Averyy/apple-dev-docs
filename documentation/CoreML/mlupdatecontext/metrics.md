# metrics

**Framework**: Core ML  
**Kind**: property

The training metrics of the model for the update task, contained in a dictionary.

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
var metrics: [MLMetricKey : Any] { get }
```

#### Discussion

Use the [`MLMetricKey`](mlmetrickey.md) to access the values within the dictionary.

## See Also

- [class MLMetricKey](mlmetrickey.md)
  A key for the metrics dictionary in an update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdatecontext/metrics)*