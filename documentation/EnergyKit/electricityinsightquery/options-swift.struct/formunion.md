# formUnion(_:)

**Framework**: EnergyKit  
**Kind**: method

Inserts the elements of another set into this option set.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
mutating func formUnion(_ other: Self)
```

#### Discussion

This method is implemented as a `|` (bitwise OR) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/options-swift.struct/formunion(_:))*