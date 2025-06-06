# contains(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the given closed range is contained within this closed range.

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
func contains(_ other: ClosedRange<Bound>) -> Bool
```

#### Return Value

`true` if `other` is wholly contained within this closed range; otherwise, `false`.

#### Discussion

The given closed range is contained within this range if its bounds are contained within this closed range.

```swift
let range = 0...10
range.contains(2...5)        // true
range.contains(2...10)       // true
range.contains(2...12)       // false
```

> **Note**: O(1)

## Parameters

- `other`: A closed range to check for containment within this   closed range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/contains(_:)-822cl)*