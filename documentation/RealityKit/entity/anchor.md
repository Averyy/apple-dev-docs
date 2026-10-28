# anchor

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The nearest ancestor entity that can act as an anchor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency var anchor: (any HasAnchoring)? { get }
```

## Discussion

This property returns `nil` if no ancestor can act as an anchor. An entity can act as an anchor if it adopts the [`HasAnchoring`](../hasanchoring.md) protocol. Just because an ancestor can be anchored doesn’t mean that it is. Inspect the [`isAnchored`](./isanchored.md) property to see if an entity (or one of its ancestors) is anchored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/anchor)*