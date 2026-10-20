# init(items:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Creates an item collection object from the specified set of top shelf items.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
init(items: [Item])
```

```objc
- (instancetype) initWithItems:(NSArray<TVTopShelfItem *> *) items;
```

#### Return Value

A new item collection object containing the specified `items`.

## Parameters

- `items`: The array of [`TVTopShelfItem`](../tvtopshelfitem.md) objects to put in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitemcollection/init(items:))*