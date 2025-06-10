# storeWhileEntityActive(_:)

**Framework**: Combine  
**Kind**: method

Retains the `Cancellable` as long as the entity is active (see `Entity.isActive`). If the entity is deactivated, the `Cancellable` is released.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func storeWhileEntityActive(_ entity: Entity)
```

#### Discussion

This method does nothing if the entity is already inactive.

Internally, this method stores an `AnyCancellable` in a transient component of the entity. The component is removed when the  event for this entity is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/cancellable/storewhileentityactive(_:))*