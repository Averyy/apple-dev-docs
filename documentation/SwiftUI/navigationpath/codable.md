# codable

**Framework**: SwiftUI  
**Kind**: property

A value that describes the contents of this path in a serializable format.

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
var codable: NavigationPath.CodableRepresentation? { get }
```

#### Discussion

This value is `nil` if any of the type-erased elements of the path don’t conform to the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) protocol.

## See Also

- [NavigationPath.CodableRepresentation](navigationpath/codablerepresentation.md)
  A serializable representation of a navigation path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationpath/codable)*