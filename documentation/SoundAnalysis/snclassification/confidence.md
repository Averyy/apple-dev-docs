# confidence

**Framework**: Sound Analysis  
**Kind**: property

The confidence value the model has in its prediction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var confidence: Double { get }
```

#### Discussion

The model assigns confidence values in the range `[0, 1.0]`, where `1.0` represents 100% confidence.

## See Also

- [var identifier: String](snclassification/identifier.md)
  A prediction label that’s one of the classifications a sound classifier’s underlying model defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassification/confidence)*