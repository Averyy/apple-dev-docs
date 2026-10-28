# init(destination:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a navigation link that presents the destination view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`init(destination:label:)`](./init%28destination,label%29-27n7s.md) instead.

## Declaration

```swift
nonisolated
init(destination: Destination, @ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View` and `Destination` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(@ContentBuilder destination: () -> Destination, @ContentBuilder label: () -> Label)
```

## Parameters

- `destination`: A view for the navigation link to present.
- `label`: A content builder to produce a label describing the `destination` to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationlink/init(destination:label:)-9dxix)*