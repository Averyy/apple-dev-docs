# isValid

**Framework**: Create ML  
**Kind**: property

A Boolean value indicating whether the metrics were calculated.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

Your metrics may be invalid if you attempt to perform evaluation on data that doesn’t match the structure of your training examples.

## See Also

- [var error: (any Error)?](mlwordtaggermetrics/error.md)
  The underlying error present when the metrics are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtaggermetrics/isvalid)*