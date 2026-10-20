# NavigationPath.CodableRepresentation

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

When a navigation path contains elements that conform to the [`Codable`](../../Swift/codable.md) protocol, you can use the path’s `CodableRepresentation` to convert the path to an external representation and to convert an external representation back into a navigation path.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)

## See Also

### Encoding a path
- [var codable: NavigationPath.CodableRepresentation?](./codable.md)
  A value that describes the contents of this path in a serializable format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationpath/codablerepresentation)*