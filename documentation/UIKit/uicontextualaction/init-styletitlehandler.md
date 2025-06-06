# init(style:title:handler:)

**Framework**: UIKit  
**Kind**: init

Creates a new contextual action with the specified title and handler.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(style: UIContextualAction.Style, title: String?, handler: @escaping UIContextualAction.Handler)
```

#### Return Value

An initialized contextual action object.

## Parameters

- `style`: The style information to apply to the action button.
- `title`: The title of the action button.
- `handler`: The handler to execute when the user selects the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextualaction/init(style:title:handler:))*