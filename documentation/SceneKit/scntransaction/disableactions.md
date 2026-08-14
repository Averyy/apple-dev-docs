# disableActions

**Framework**: SceneKit  
**Kind**: property

Returns a Boolean value indicating whether changes to animatable properties during the transaction are implicitly animated.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class var disableActions: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if implicit animation is disabled; [`false`](https://developer.apple.com/documentation/swift/false) if implicit animation is allowed.

#### Discussion

By default (when this property is [`false`](https://developer.apple.com/documentation/swift/false)), any changes to animatable properties of objects in the scene graph implicitly create animations. (These animations may not be visible unless you use the [`animationDuration`](scntransaction/animationduration.md) property to set a nonzero duration for the transaction.) Set this property to [`true`](https://developer.apple.com/documentation/swift/true) to disable implicit animation during the transaction.

Disabling animation applies to all property changes in the current transaction and any nested transactions within it. However, you can use this property again within a nested transaction to enable implicit animation for that transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/disableactions)*