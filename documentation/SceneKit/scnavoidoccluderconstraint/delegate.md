# delegate

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

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
unowned(unsafe) var delegate: any SCNAvoidOccluderConstraintDelegate { get set }
```

```objc
@property (nonatomic, assign) id<SCNAvoidOccluderConstraintDelegate> delegate;
```

## See Also

### Configuring Constraint Behavior
- [var bias: CGFloat](./bias.md)
- [var occluderCategoryBitMask: Int](./occludercategorybitmask.md)
- [var target: SCNNode?](./target.md)
- [protocol SCNAvoidOccluderConstraintDelegate](../scnavoidoccluderconstraintdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnavoidoccluderconstraint/delegate)*