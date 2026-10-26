# removeFirst()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes and returns the first element of the collection.

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
@discardableResult
mutating func removeFirst() -> Self.Element
```

Available when `Self` is `Self.SubSequence`.

#### Return Value

The first element of the collection.

#### Discussion

The collection must not be empty.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> **Complexity**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/removefirst()-6z962)*