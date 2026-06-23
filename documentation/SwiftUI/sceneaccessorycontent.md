# SceneAccessoryContent

**Framework**: SwiftUI  
**Kind**: protocol

Conforming types represent items which define content for scene accessories.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol SceneAccessoryContent
```

## Topics

### Associated Types
- [associatedtype Body : SceneAccessoryContent](sceneaccessorycontent/body-swift.associatedtype.md)
  The type of content representing the body of this scene accessory content.
### Instance Properties
- [var body: Self.Body](sceneaccessorycontent/body-swift.property.md)
  The composition of content that comprise the accessory content.
### Instance Methods
- [func onAvailabilityChange(perform: (Bool) -> Void) -> some SceneAccessoryContent](sceneaccessorycontent/onavailabilitychange(perform:).md)
  Defines a callback for observing the availability of `self`.

## Relationships

### Conforming Types
- [EmptyView](emptyview.md)
- [ExternalNonInteractiveAccessory](externalnoninteractiveaccessory.md)
- [ForEach](foreach.md)
- [Group](group.md)
- [TupleContent](tuplecontent.md)

## See Also

- [func sceneAccessory<C>(content: () -> C) -> some View](view/sceneaccessory(content:).md)
  Defines any scene accessories associated with `self`.
- [struct ExternalNonInteractiveAccessory](externalnoninteractiveaccessory.md)
  A scene accessory that presents non-interactive content on an external display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sceneaccessorycontent)*