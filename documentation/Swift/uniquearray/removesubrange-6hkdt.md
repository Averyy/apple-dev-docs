# removeSubrange(_:)

**Framework**: Swift  
**Kind**: method

Removes the specified subrange of elements from the array.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func removeSubrange(_ bounds: some RangeExpression<Int>)
```

#### Discussion

> **Note**: O(`self.count`)

## Parameters

- `bounds`: The subrange of the array to remove. The bounds of the range must be valid indices of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/removesubrange(_:)-6hkdt)*