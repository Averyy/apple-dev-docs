# isPresented

**Framework**: RealityKit  
**Kind**: property

A boolean value that indicates whether the content is presented.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var isPresented: Bool { get set }
```

#### Discussion

If you initialize the component with a binding, that binding will mirror the value of this property. If the component is initialized without a binding, this property will default to `true`.

When the presentation is dismissed by the system, the system will set this value to `false`, and trigger a `ComponentEvents.DidChange` event. Setting this value back to `true` will cause the modal to be presented again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/presentationcomponent/ispresented)*