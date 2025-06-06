# init(make:update:)

**Framework**: RealityKit  
**Kind**: init

Creates a new reality view for visionOS with an optional update closure.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(make: @escaping @MainActor (inout RealityViewContent) async -> Void, update: (@MainActor (inout RealityViewContent) -> Void)? = nil) where Content == RealityViewContent.Body<RealityViewDefaultPlaceholder>
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

- [init<P>(make: (inout RealityViewContent) async -> Void, update: ((inout RealityViewContent) -> Void)?, placeholder: () -> P)](realityview/init(make:update:placeholder:)-4c8yv.md)
  Creates a new reality view for visionOS with an optional update closure and placeholder view.
- [init<A>(make: (inout RealityViewContent, RealityViewAttachments) async -> Void, update: ((inout RealityViewContent, RealityViewAttachments) -> Void)?, attachments: () -> A)](realityview/init(make:update:attachments:).md)
  Creates a reality view for visionOS, with attachments and an optional update closure.
- [init<A, P>(make: (inout RealityViewContent, RealityViewAttachments) async -> Void, update: ((inout RealityViewContent, RealityViewAttachments) -> Void)?, placeholder: () -> P, attachments: () -> A)](realityview/init(make:update:placeholder:attachments:).md)
  Creates a reality view for visionOS, with attachments, an optional update closure, and placeholder view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/init(make:update:)-666xr)*