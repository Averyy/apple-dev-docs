# hideObjectReticle(_:)

**Framework**: RealityKit  
**Kind**: method

Hides the object selection reticle when the session is in `.ready` state if set to true. Example: ObjectCaptureView(session: mySession) .hideObjectReticle()

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func hideObjectReticle(_ value: Bool = true) -> ObjectCaptureView<Overlay>
```

#### Discussion

It can also be passed a value if there is a state variable controlling it:

ObjectCaptureView(session: mySession) .hideObjectReticle(shouldHideObjectReticle)

Other modifiers can be chained to build the final view: ObjectCaptureView(session: mySession) .hideObjectReticle() .transition(.opacity)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcaptureview/hideobjectreticle(_:))*