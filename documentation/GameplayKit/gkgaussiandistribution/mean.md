# mean

**Framework**: GameplayKit  
**Kind**: property

The mean value of the distribution (also called the  or ).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var mean: Float { get }
```

#### Discussion

Random samplings from the distribution are most likely to result in the mean value, with other values increasingly far from the mean occurring with decreasing probability.

This property is read-only—its value is always the midpoint between the values of the inherited [`lowestValue`](gkrandomdistribution/lowestvalue.md) and [`highestValue`](gkrandomdistribution/highestvalue.md) properties (`mean = (highest + lowest) / 2`).

## See Also

- [var deviation: Float](gkgaussiandistribution/deviation.md)
  The standard deviation of the distribution (also called ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgaussiandistribution/mean)*