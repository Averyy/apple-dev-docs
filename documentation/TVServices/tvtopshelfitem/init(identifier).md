# init(identifier:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Creates a top shelf item with the specified identifier.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
init(identifier: String)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier;
```

#### Return Value

An empty item object.

#### Discussion

After creating the item object, call the [`setImageURL(_:for:)`](./setimageurl%28_,for%29.md) method to assign an image and one or more actions to the item. Include the item object in the [`TVTopShelfContent`](../tvtopshelfcontent.md) object you return from your extension.

## Parameters

- `identifier`: The string you use to identify this item. This string must be unique among all of the items you ever return from your app. Never recycle identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitem/init(identifier:))*