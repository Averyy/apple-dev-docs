# init(destination:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents the destination view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@export(implementation)
nonisolated init(@ContentBuilder destination: () -> Destination, @ContentBuilder label: () -> Label)
```

**Other overloads**:

```swift
nonisolated
init(destination: Destination, @ContentBuilder label: () -> Label)
```

## Parameters

- `destination`: A view for the navigation link to present.
- `label`: A content builder to produce a label describing the `destination` to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destination:label:)-27n7s)*