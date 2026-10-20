# init(title:action:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a menu-item object initialized with the given title and action.

**Availability**:
- iOS 3.2+ - Deprecated in 16.0
- iPadOS 3.2+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For more information, see [`UIMenuItem`](../uimenuitem.md).

## Declaration

```swift
init(title: String, action: Selector)
```

```objc
- (instancetype) initWithTitle:(NSString *) title action:(SEL) action;
```

#### Return Value

An initialized `UIMenuItem` object, or `nil` if there was a problem creating the object.

## Parameters

- `title`: The title of the menu item.
- `action`: A selector identifying the method of the responder object to invoke for handling the command represented by the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuitem/init(title:action:))*