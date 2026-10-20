# disableActions

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Returns a Boolean value indicating whether changes to animatable properties during the transaction are implicitly animated.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class var disableActions: Bool { get set }
```

```objc
@property (class, nonatomic) BOOL disableActions;
```

#### Return Value

[`true`](../../Swift/true.md) if implicit animation is disabled; [`false`](../../Swift/false.md) if implicit animation is allowed.

#### Discussion

By default (when this property is [`false`](../../Swift/false.md)), any changes to animatable properties of objects in the scene graph implicitly create animations. (These animations may not be visible unless you use the [`animationDuration`](./animationduration.md) property to set a nonzero duration for the transaction.) Set this property to [`true`](../../Swift/true.md) to disable implicit animation during the transaction.

Disabling animation applies to all property changes in the current transaction and any nested transactions within it. However, you can use this property again within a nested transaction to enable implicit animation for that transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/disableactions)*