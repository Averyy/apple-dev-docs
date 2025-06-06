# entity(for:)

**Framework**: RealityKit  
**Kind**: method

Gets the identified attachment view as an entity, if the view with that identifier exists.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
func entity(for id: some Hashable) -> ViewAttachmentEntity?
```

#### Return Value

The resolved attachment entity, or `nil` if [`RealityView`](realityview.md) can’t find an attachment view with the given `id`.

#### Discussion

Attachment entities are not automatically added to your [`RealityView`](realityview.md)’s content. To display an attachment, add it to your [`RealityView`](realityview.md)’s content using a function like [`add(_:)`](realityviewcontent/add(_:).md).

## Parameters

- `id`: The value that you used to tag the view when you   define it in the   parameter of the    initializer  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewattachments/entity(for:))*