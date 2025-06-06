# NavigationPath.CodableRepresentation

**Framework**: SwiftUI  
**Kind**: struct

A serializable representation of a navigation path.

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
struct CodableRepresentation
```

#### Overview

When a navigation path contains elements the conform to the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) protocol, you can use the path’s `CodableRepresentation` to convert the path to an external representation and to convert an external representation back into a navigation path.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [var codable: NavigationPath.CodableRepresentation?](navigationpath/codable.md)
  A value that describes the contents of this path in a serializable format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationpath/codablerepresentation)*