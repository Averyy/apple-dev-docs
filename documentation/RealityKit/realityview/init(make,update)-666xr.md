# init(make:update:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a new reality view for visionOS with an optional update closure.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(make: @escaping @MainActor @Sendable (inout RealityViewContent) async -> Void, update: (@MainActor (inout RealityViewContent) -> Void)? = nil) where Content == RealityViewContent.Body<RealityViewDefaultPlaceholder>
```

Available when `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(make: @escaping @MainActor @Sendable (inout RealityViewCameraContent) async -> Void, update: (@MainActor (inout RealityViewCameraContent) -> Void)? = nil) where Content == RealityViewCameraContent.Body<RealityViewDefaultPlaceholder>
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

- `make`: An asynchronous closure that configures the initial content of the new `RealityView`. This closure is asynchronous to keep your app’s UI responsive while you load content to populate this view.
- `update`: An optional closure that updates the `RealityView` instance’s content as the view’s state changes.

## See Also

### Creating a reality view for visionOS
- [init<P>(make: (inout RealityViewContent) async -> Void, update: ((inout RealityViewContent) -> Void)?, placeholder: () -> P)](./init%28make,update,placeholder%29-4c8yv.md)
  Creates a new reality view for visionOS with an optional update closure and placeholder view.
- [init<A>(make: (inout RealityViewContent, RealityViewAttachments) async -> Void, update: ((inout RealityViewContent, RealityViewAttachments) -> Void)?, attachments: () -> A)](./init%28make,update,attachments%29.md)
  Creates a reality view for visionOS, with attachments and an optional update closure.
- [init<A, P>(make: (inout RealityViewContent, RealityViewAttachments) async -> Void, update: ((inout RealityViewContent, RealityViewAttachments) -> Void)?, placeholder: () -> P, attachments: () -> A)](./init%28make,update,placeholder,attachments%29.md)
  Creates a reality view for visionOS, with attachments, an optional update closure, and placeholder view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/init(make:update:)-666xr)*