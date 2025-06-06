# append(_:)

**Framework**: Swift  
**Kind**: method

Adds a new element at the end of the array.

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
mutating func append(_ newElement: Element)
```

#### Discussion

Use this method to append a single element to the end of a mutable array.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(100)
print(numbers)
// Prints "[1, 2, 3, 4, 5, 100]"
```

Because arrays increase their allocated capacity using an exponential strategy, appending a single element to an array is an O(1) operation when averaged over many calls to the `append(_:)` method. When an array has additional capacity and is not sharing its storage with another instance, appending an element is O(1). When an array needs to reallocate storage before appending or its storage is shared with another copy, appending is O(), where  is the length of the array.

> **Note**: O(1) on average, over many calls to `append(_:)` on the same array.

O(1) on average, over many calls to `append(_:)` on the same array.

## Parameters

- `newElement`: The element to append to the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/append(_:))*