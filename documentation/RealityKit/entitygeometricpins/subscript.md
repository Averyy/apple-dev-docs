# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Obtains a geometric pin the entity owns by name.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
subscript(name: String) -> GeometricPin? { get }
```

#### Return Value

The pin that associates with the name, or `nil` if no pin with a matching name is found.

## Parameters

- `name`: The name of an existing pin the entity owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitygeometricpins/subscript(_:))*