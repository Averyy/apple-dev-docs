# SceneAccessoryContent

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

Conforming types represent items which define content for scene accessories.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
@MainActor
protocol SceneAccessoryContent
```

## Topics

### Associated Types
- [associatedtype Body : SceneAccessoryContent](./sceneaccessorycontent/body-swift.associatedtype.md)
  The type of content representing the body of this scene accessory content.
### Instance Properties
- [var body: Self.Body](./sceneaccessorycontent/body-swift.property.md)
  The composition of content that comprise the accessory content.
### Instance Methods
- [func onAvailabilityChange(perform: (Bool) -> Void) -> some SceneAccessoryContent](./sceneaccessorycontent/onavailabilitychange%28perform%29.md)
  Defines a callback for observing the availability of `self`.

## Relationships

### Conforming Types
- [CameraCaptureAccessory](./cameracaptureaccessory.md)
- [EmptyView](./emptyview.md)
- [ExternalNonInteractiveAccessory](./externalnoninteractiveaccessory.md)
- [ForEach](./foreach.md)
- [Group](./group.md)
- [TupleContent](./tuplecontent.md)

## See Also

### Presenting content on an external display
- [func sceneAccessory<C>(content: () -> C) -> some View](./view/sceneaccessory%28content%29.md)
  Defines any scene accessories associated with `self`.
- [struct CameraCaptureAccessory](./cameracaptureaccessory.md)
  A scene accessory that presents content during camera capture.
- [struct ExternalNonInteractiveAccessory](./externalnoninteractiveaccessory.md)
  A scene accessory that presents non-interactive content on an external display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sceneaccessorycontent)*