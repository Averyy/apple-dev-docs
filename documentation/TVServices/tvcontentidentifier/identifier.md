# identifier

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

The string that identifies this content item.

**Availability**:
- tvOS 9.0+ - Deprecated in 13.0

> **Deprecated**: TVContentIdentifier has been replaced by TVTopShelfContentProvider

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

#### Discussion

The contents of this string are defined by you when you design your application.

## See Also

### Inspecting an Identifier’s Contents
- [var container: TVContentIdentifier?](./container.md)
  The container that this content item is contained in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentidentifier/identifier)*