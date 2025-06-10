# removeLast(_:)

**Framework**: SwiftUI  
**Kind**: method

Removes values from the end of this path.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
mutating func removeLast(_ k: Int = 1)
```

#### Discussion

> **Note**: The input parameter `k` must be greater than or equal to zero, and must be less than or equal to the number of elements in the path.

## Parameters

- `k`: The number of values to remove. The default value is  .

## See Also

- [var isEmpty: Bool](navigationpath/isempty.md)
  A Boolean that indicates whether this path is empty.
- [var count: Int](navigationpath/count.md)
  The number of elements in this path.
- [func append(_:)](navigationpath/append(_:).md)
  Appends a new codable value to the end of this path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationpath/removelast(_:))*