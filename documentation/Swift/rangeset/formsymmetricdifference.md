# formSymmetricDifference(_:)

**Framework**: Swift  
**Kind**: method

Removes the contents of this range set that are also in the given set and adds the contents of the given set that are not already in this range set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func formSymmetricDifference(_ other: RangeSet<Bound>)
```

## Parameters

- `other`: A range set to perform a symmetric difference against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/formsymmetricdifference(_:))*