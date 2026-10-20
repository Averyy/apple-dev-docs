# ..<(_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns a partial range up to, but not including, its upper bound.

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
static func ..< (maximum: Self) -> PartialRangeUpTo<Self>
```

#### Discussion

Use the prefix half-open range operator (prefix `..<`) to create a partial range of any type that conforms to the `Comparable` protocol. This example creates a `PartialRangeUpTo<Double>` instance that includes any value less than `5.0`.

```swift
let upToFive = ..<5.0

upToFive.contains(3.14)       // true
upToFive.contains(6.28)       // false
upToFive.contains(5.0)        // false
```

You can use this type of partial range of a collection’s indices to represent the range from the start of the collection up to, but not including, the partial range’s upper bound.

```swift
let numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[..<3])
// Prints "[10, 20, 30]"
```

> **Precondition**: `maximum` must compare equal to itself (i.e. cannot be NaN).

## Parameters

- `maximum`: The upper bound for the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablepointer/'.._(_:))*