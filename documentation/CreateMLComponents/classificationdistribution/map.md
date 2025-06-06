# map(_:)

**Framework**: Create ML Components  
**Kind**: method

Creates a new classification distribution by applying a transformation to every element.

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
func map<T>(_ transform: (Classification<Label>) throws -> Classification<T>) rethrows -> ClassificationDistribution<T> where T : Hashable
```

## Parameters

- `transform`: A transformation closure.

## See Also

- [func topLabels(Int) -> [Label]](classificationdistribution/toplabels(_:).md)
  Computes the most likely labels in the classification set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution/map(_:))*