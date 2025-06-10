# formSymmetricDifference(_:)

**Framework**: EnergyKit  
**Kind**: method

Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
mutating func formSymmetricDifference(_ other: Self)
```

#### Discussion

This method is implemented as a `^` (bitwise XOR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/options-swift.struct/formsymmetricdifference(_:))*