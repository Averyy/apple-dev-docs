# action

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A selector identifying the method of the responder object to invoke for handling of the menu command.

**Availability**:
- iOS 3.2+ - Deprecated in 16.0
- iPadOS 3.2+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For more information, see [`UIMenuItem`](../uimenuitem.md).

## Declaration

```swift
var action: Selector { get set }
```

```objc
@property (nonatomic) SEL action;
```

#### Discussion

The action selector cannot be `NULL`.

## See Also

### Accessing menu-item attributes
- [var title: String](./title.md)
  The title of the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuitem/action)*