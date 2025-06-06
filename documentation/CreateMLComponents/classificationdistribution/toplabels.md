# topLabels(_:)

**Framework**: Create ML Components  
**Kind**: method

Computes the most likely labels in the classification set.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func topLabels(_ amount: Int) -> [Label]
```

#### Return Value

The labels with the highest probabilities.

## Parameters

- `amount`: The number of top labels.

## See Also

- [func map<T>((Classification<Label>) throws -> Classification<T>) rethrows -> ClassificationDistribution<T>](classificationdistribution/map(_:).md)
  Creates a new classification distribution by applying a transformation to every element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/toplabels(_:))*