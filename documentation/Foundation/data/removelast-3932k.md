# removeLast()

**Framework**: Foundation  
**Kind**: method

Removes and returns the last element of the collection.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@discardableResult
mutating func removeLast() -> Self.Element
```

#### Return Value

The last element of the collection.

#### Discussion

The collection must not be empty.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/removelast()-3932k)*