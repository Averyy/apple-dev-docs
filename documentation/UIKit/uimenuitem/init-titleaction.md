# init(title:action:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a menu-item object initialized with the given title and action.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(title: String, action: Selector)
```

#### Return Value

An initialized `UIMenuItem` object, or `nil` if there was a problem creating the object.

## Parameters

- `title`: The title of the menu item.
- `action`: A selector identifying the method of the responder object to invoke for handling the command represented by the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuitem/init(title:action:))*