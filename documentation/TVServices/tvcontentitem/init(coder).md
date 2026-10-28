# init(coder:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Returns an object initialized from data in a given unarchiver.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentItem has been replaced by TVTopShelfItem

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Return Value

A newly initialized content  object.

## Parameters

- `coder`: An unarchiver object.

## See Also

### Initializing a Content Item
- [init(contentIdentifier: TVContentIdentifier)](./init%28contentidentifier%29.md)
  Initializes a new content item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/init(coder:))*