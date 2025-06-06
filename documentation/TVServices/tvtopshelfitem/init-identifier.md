# init(identifier:)

**Framework**: TV Services  
**Kind**: init

Creates a top shelf item with the specified identifier.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
init(identifier: String)
```

#### Return Value

An empty item object.

#### Discussion

After creating the item object, call the [`setImageURL(_:for:)`](tvtopshelfitem/setimageurl(_:for:).md) method to assign an image and one or more actions to the item. Include the item object in the [`TVTopShelfContent`](tvtopshelfcontent.md) object you return from your extension.

## Parameters

- `identifier`: The string you use to identify this item. This string must be unique among all of the items you ever return from your app. Never recycle identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitem/init(identifier:))*