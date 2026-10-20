# init(coder:)

**Framework**: TV Services  
**Kind**: init  
**Role**: Initializer

Returns an object initialized from data in a given unarchiver.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentIdentifier has been replaced by TVTopShelfContentProvider

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

#### Return Value

A newly initialized content identifier object.

## Parameters

- `coder`: An unarchiver object.

## See Also

### Initializing a Content Identifier
- [init(identifier: String, container: TVContentIdentifier?)](./init%28identifier,container%29.md)
  Creates a new content identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentidentifier/init(coder:))*