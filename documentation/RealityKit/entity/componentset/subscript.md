# subscript(_:_:)

**Framework**: RealityKit  
**Kind**: subscript

Gets or sets the component of the specified type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency subscript<T>(componentType: T.Type, backDeploy: Void = ()) -> T? where T : Component { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/subscript(_:_:))*