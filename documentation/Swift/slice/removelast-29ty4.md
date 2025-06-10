# removeLast()

**Framework**: Swift  
**Kind**: method

Removes and returns the last element of the collection.

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
mutating func removeLast() -> Self.Element
```

#### Return Value

The last element of the collection.

#### Discussion

The collection must not be empty. To remove the last element of a collection that might be empty, use the `popLast()` method instead.

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/removelast()-29ty4)*