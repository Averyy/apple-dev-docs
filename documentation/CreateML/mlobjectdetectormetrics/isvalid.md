# isValid

**Framework**: Create ML  
**Kind**: property

A Boolean value indicating whether the object detector model was able to calculate metrics.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

Your metrics may be invalid if you attempt to perform evaluation on images with annotations that don’t match the annotations of your training examples.

## See Also

- [var error: (any Error)?](mlobjectdetectormetrics/error.md)
  The underlying error present when the metrics are invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics/isvalid)*