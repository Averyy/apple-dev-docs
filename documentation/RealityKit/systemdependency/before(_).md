# SystemDependency.before(_:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

An update order that requests RealityKit update this system before it updates another specified system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
case before(any System.Type)
```

## Mentions

- [Implementing systems for entities in a scene](../implementing-systems-for-entities-in-a-scene.md)

## Parameters

- `System`: A system that this system updates before.

## See Also

### Update order
- [case after(any System.Type)](./after%28_%29.md)
  An update order that requests RealityKit update this system after it updates another specified system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/systemdependency/before(_:))*