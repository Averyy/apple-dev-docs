# init(make:update:attachments:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a reality view for visionOS, with attachments and an optional update closure.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<A>(make: @escaping @MainActor @Sendable (inout RealityViewContent, RealityViewAttachments) async -> Void, update: (@MainActor (inout RealityViewContent, RealityViewAttachments) -> Void)? = nil, @AttachmentContentBuilder attachments: @escaping () -> A) where Content == RealityViewAttachmentBuilderContent<A, RealityViewContent.Body<RealityViewDefaultPlaceholder>>, A : AttachmentContent
```

Available when `Content` conforms to `View`.

#### Discussion

This initializer doesn’t automatically add the attachment views to your [`RealityViewContent`](../realityviewcontent.md). You can access the entities that represent the attachments by calling the [`entity(for:)`](../realityviewattachments/entity%28for%29.md) method of the [`RealityViewAttachments`](../realityviewattachments.md), and add them to your content or as a child of another [`Entity`](../entity.md):

```swift
RealityView { content, attachments in
    if let attachment = attachments.entity(for: "example") {
        content.add(attachment)
    }
} attachments: {
    Attachment(id: "example") {
        Text("hello")
    }
}
```

## Parameters

- `make`: An asynchronous closure that configures the initial content of the new `RealityView`. This closure is asynchronous to keep your app’s UI responsive while you load content to populate this view.
- `update`: An optional closure that updates the `RealityView` instance’s content as the view’s state changes.
- `attachments`: An attachment content builder that adds attachment views to the content of the `RealityView`.

## See Also

### Creating a reality view for visionOS
- [init(make: (inout RealityViewContent) async -> Void, update: ((inout RealityViewContent) -> Void)?)](./init%28make,update%29-666xr.md)
  Creates a new reality view for visionOS with an optional update closure.
- [init<P>(make: (inout RealityViewContent) async -> Void, update: ((inout RealityViewContent) -> Void)?, placeholder: () -> P)](./init%28make,update,placeholder%29-4c8yv.md)
  Creates a new reality view for visionOS with an optional update closure and placeholder view.
- [init<A, P>(make: (inout RealityViewContent, RealityViewAttachments) async -> Void, update: ((inout RealityViewContent, RealityViewAttachments) -> Void)?, placeholder: () -> P, attachments: () -> A)](./init%28make,update,placeholder,attachments%29.md)
  Creates a reality view for visionOS, with attachments, an optional update closure, and placeholder view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/init(make:update:attachments:))*