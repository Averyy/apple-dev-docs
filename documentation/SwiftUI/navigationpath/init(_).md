# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new navigation path from a serializable version.

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
init(_ codable: NavigationPath.CodableRepresentation)
```

**Other overloads**:

```swift
init<S>(_ elements: S) where S : Sequence, S.Element : Decodable, S.Element : Encodable, S.Element : Hashable
```

```swift
init<S>(_ elements: S) where S : Sequence, S.Element : Hashable
```

## Parameters

- `codable`: A value describing the contents of the new path in a serializable format.

## See Also

### Creating a navigation path
- [init()](./init%28%29.md)
  Creates a new, empty navigation path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationpath/init(_:))*