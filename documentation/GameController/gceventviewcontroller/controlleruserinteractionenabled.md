# controllerUserInteractionEnabled

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the system delivers game controller input to profile objects or to views using the responder chain.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var controllerUserInteractionEnabled: Bool { get set }
```

#### Discussion

If this property is [`false`](https://developer.apple.com/documentation/swift/false), when the view controller’s view or its subviews are the first responder, the system delivers the game controller input to the profile objects. If this property is [`true`](https://developer.apple.com/documentation/swift/true), the system generates input events and delivers them through the responder chain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller/controlleruserinteractionenabled)*