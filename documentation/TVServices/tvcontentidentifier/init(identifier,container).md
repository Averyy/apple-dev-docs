# init(identifier:container:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Creates a new content identifier.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentIdentifier has been replaced by TVTopShelfContentProvider

## Declaration

```swift
init(identifier: String, container: TVContentIdentifier?)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier container:(TVContentIdentifier *) container;
```

#### Return Value

A newly initialized content identifier object.

## Parameters

- `identifier`: The string to be used as the identifier.
- `container`: The container (if any) that contains the content.

## See Also

### Initializing a Content Identifier
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns an object initialized from data in a given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentidentifier/init(identifier:container:))*