# useParentedControllers

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether to parent the new animation’s controller to the controller managing this action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var useParentedControllers: Bool
```

#### Discussion

Setting the value of this property to true indicates the action has control over the playback of the animation. Setting this to false indicates the animation plays independently from the action, behaving as a one shot animation


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/playanimationaction/useparentedcontrollers)*