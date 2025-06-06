# formUnion(_:)

**Framework**: Swift  
**Kind**: method

Adds the contents of the given range set to this range set.

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
mutating func formUnion(_ other: RangeSet<Bound>)
```

#### Discussion

> **Note**: O( + ), where  and  are the number of ranges in this and the other range set.

O( + ), where  and  are the number of ranges in this and the other range set.

## Parameters

- `other`: A range set to merge with this one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangeset/formunion(_:))*