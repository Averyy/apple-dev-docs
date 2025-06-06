# formIntersection(_:)

**Framework**: Group Activities  
**Kind**: method

Removes all elements of this option set that are not also present in the given set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func formIntersection(_ other: Self)
```

#### Discussion

This method is implemented as a `&` (bitwise AND) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/broadcastoptions/formintersection(_:))*