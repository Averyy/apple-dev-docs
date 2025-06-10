# formSymmetricDifference(_:)

**Framework**: Swift  
**Kind**: method

Replaces this set with a new set containing all elements contained in either this set or the given set, but not in both.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func formSymmetricDifference(_ other: Self)
```

#### Discussion

This method is implemented as a `^` (bitwise XOR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clocktraits/formsymmetricdifference(_:))*