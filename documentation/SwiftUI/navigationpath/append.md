# append(_:)

**Framework**: SwiftUI  
**Kind**: method

Appends a new codable value to the end of this path.

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
mutating func append<V>(_ value: V) where V : Decodable, V : Encodable, V : Hashable
```

## Mentions

- [Understanding the navigation stack](understanding-the-composition-of-navigation-stack.md)

## See Also

- [var isEmpty: Bool](navigationpath/isempty.md)
  A Boolean that indicates whether this path is empty.
- [var count: Int](navigationpath/count.md)
  The number of elements in this path.
- [func removeLast(Int)](navigationpath/removelast(_:).md)
  Removes values from the end of this path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationpath/append(_:))*