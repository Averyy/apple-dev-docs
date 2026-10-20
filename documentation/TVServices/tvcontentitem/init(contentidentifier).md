# init(contentIdentifier:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Initializes a new content item.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
init(contentIdentifier ident: TVContentIdentifier)
```

```objc
- (instancetype) initWithContentIdentifier:(TVContentIdentifier *) ident;
```

#### Return Value

A new content item.

## Parameters

- `ident`: The identifier for the new content item.

## See Also

### Initializing a Content Item
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns an object initialized from data in a given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/init(contentidentifier:))*