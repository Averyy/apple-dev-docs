# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new navigation path from the contents of a sequence.

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
init<S>(_ elements: S) where S : Sequence, S.Element : Hashable
```

**Other overloads**:

```swift
init(_ codable: NavigationPath.CodableRepresentation)
```

```swift
init<S>(_ elements: S) where S : Sequence, S.Element : Decodable, S.Element : Encodable, S.Element : Hashable
```

## Parameters

- `elements`: A sequence used to create the navigation path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationpath/init(_:)-dfls)*