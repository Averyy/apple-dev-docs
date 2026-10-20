# orientationConstraint(inWorldSpace:with:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

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
class func orientationConstraint(inWorldSpace world: Bool, with block: @escaping (SCNNode, SCNQuaternion) -> SCNQuaternion) -> Self
```

```objc
+ (instancetype) orientationConstraintInWorldSpace:(BOOL) world withBlock:(SCNQuaternion (^)(SCNNode *node, SCNQuaternion quaternion)) block;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransformconstraint/orientationconstraint(inworldspace:with:))*