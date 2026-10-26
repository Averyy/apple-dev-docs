# formIntersection(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes all elements of this option set that are not also present in the given set.

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
mutating func formIntersection(_ other: Self)
```

Available when `RawValue` conforms to `FixedWidthInteger`.

#### Discussion

This method is implemented as a `&` (bitwise AND) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/formintersection(_:)-9h7lm)*