# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript  
**Role**: Instance Subscript

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
subscript<T>(type: T.Type) -> T? where T : Component { get set }
```

**Other overloads**:

```swift
subscript<T>(componentType: T.Type) -> T? where T : _ImplicitlyAnimatableBuiltinComponent { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/observable-swift.struct/components-swift.struct/subscript(_:)-7alu8)*