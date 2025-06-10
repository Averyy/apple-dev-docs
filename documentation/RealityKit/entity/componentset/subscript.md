# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Gets or sets the component with a specific dynamically supplied type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency subscript(componentType: any Component.Type) -> (any Component)? { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/subscript(_:))*