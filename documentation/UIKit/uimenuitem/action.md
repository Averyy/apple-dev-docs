# action

**Framework**: UIKit  
**Kind**: property

A selector identifying the method of the responder object to invoke for handling of the menu command.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var action: Selector { get set }
```

#### Discussion

The action selector cannot be `NULL`.

## See Also

- [var title: String](uimenuitem/title.md)
  The title of the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuitem/action)*