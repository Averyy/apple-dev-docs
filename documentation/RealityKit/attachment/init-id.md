# init(id:_:)

**Framework**: RealityKit  
**Kind**: init

Creates an new attachment from an identifier and a closure.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(id: AnyHashable, @ViewBuilder _ content: @escaping () -> Content)
```

#### Discussion

You can access details of an attachment entity, such as its bounds, by calling the methods of a [`ViewAttachmentEntity`](viewattachmententity.md) instance. For example, you can add an attachment that contains the text `"hello"`.

```swift
Attachment(id: "example") {
    Text("hello")
}
```

> **Note**: The initializer doesn’t automatically add the views to a [`RealityView`](realityview.md) instance. You need to explicitly add each entity to your app’s scene hierarchy by directly placing an entity attachment to the view or as a child of another entity that’s already in the view.

## Parameters

- `id`: An   instance that identifies the attachment and   a  .
- `content`: A   instance that contains the views for the   attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/attachment/init(id:_:))*