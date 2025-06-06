# isValid

**Framework**: Create ML  
**Kind**: property

A Boolean value indicating whether the regressor model was able to calculate metrics.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

Your metrics may be invalid if you attempt to perform evaluation on data that doesn’t match the structure of your training examples.

## See Also

- [var error: (any Error)?](mlregressormetrics/error.md)
  The underlying error present when the metrics are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressormetrics/isvalid)*