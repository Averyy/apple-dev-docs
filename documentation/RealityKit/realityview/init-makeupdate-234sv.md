# init(make:update:)

**Framework**: RealityKit  
**Kind**: init

Creates a reality view for iOS and macOS, with an optional update closure.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
nonisolated
init(make: @escaping @MainActor (inout RealityViewCameraContent) async -> Void, update: (@MainActor (inout RealityViewCameraContent) -> Void)? = nil) where Content == RealityViewCameraContent.Body<RealityViewDefaultPlaceholder>
```

#### Discussion

Use the `update` closure to modify entities in the scene based on a Boolean state property, like in the following example:

```swift
RealityView { content in
    content.add(boxEntity)
} update: { content in
    boxEntity.scale = isEnlarged ? .one * 2 : .one
}
```

## Parameters

- `make`: An asynchronous closure that configures the   initial content of the new  .   This closure is asynchronous to keep your app’s UI responsive while   you load content to populate this view.
- `update`: An optional closure that updates the    instance’s content as the view’s state changes.

## See Also

- [init<P>(make: (inout RealityViewCameraContent) async -> Void, update: ((inout RealityViewCameraContent) -> Void)?, placeholder: () -> P)](realityview/init(make:update:placeholder:)-4x7ds.md)
  Creates a reality view for iOS and macOS, with an optional update closure and placeholder view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/init(make:update:)-234sv)*