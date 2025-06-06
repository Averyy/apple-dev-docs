# append(_:)

**Framework**: Swift  
**Kind**: method

Adds an element to the end of the collection.

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
mutating func append(_ newElement: Self.Element)
```

#### Discussion

If the collection does not have sufficient capacity for another element, additional storage is allocated before appending `newElement`. The following example adds a new number to an array of integers:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(100)

print(numbers)
// Prints "[1, 2, 3, 4, 5, 100]"
```

> **Note**: O(1) on average, over many calls to `append(_:)` on the same collection.

## Parameters

- `newElement`: The element to append to the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/append(_:)-1re5n)*