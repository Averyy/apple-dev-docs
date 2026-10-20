# radius

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The radius of the wheel.

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
var radius: CGFloat { get set }
```

```objc
@property CGFloat radius;
```

#### Discussion

When you create a wheel from a node, its default radius is half of the largest dimension of the node’s bounding box. (A wheel is always circular, even if the content of the node representing it is not.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/radius)*