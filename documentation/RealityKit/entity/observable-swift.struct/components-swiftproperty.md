# components

**Framework**: RealityKit  
**Kind**: property

The components an entity manages, enabling observation of their presence and values.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var components: Entity.Observable.Components { get set }
```

#### Discussion

This property provides a direct interface to the entity’s components. When you read a component through this property’s accessor, it marks that component type as accessed for observation. Observers trigger when you modify any accessed component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/observable-swift.struct/components-swift.property)*