# init(items:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Creates an inset content object and populates it with the specified set of items.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
init(items: [TVTopShelfItem])
```

```objc
- (instancetype) initWithItems:(NSArray<TVTopShelfItem *> *) items;
```

## Return Value

A new inset content object containing the specified set of items.

## Parameters

- `items`: An array of [`TVTopShelfItem`](../tvtopshelfitem.md) objects representing the content that you want to display in the top shelf. This method stores a copy of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfinsetcontent/init(items:))*