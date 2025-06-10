# resource

**Framework**: RealityKit  
**Kind**: property

Reference to the resource describing the desired inverse kinematics setup.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var resource: IKResource?
```

#### Discussion

> **Note**: There is one engine tick delay between setting new resource and the change reflected in `solvers`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/resource)*