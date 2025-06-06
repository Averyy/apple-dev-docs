# init(delegate:)

**Framework**: UIKit  
**Kind**: init

Creates a context menu interaction object with the specified delegate object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(delegate: any UIContextMenuInteractionDelegate)
```

#### Return Value

A new context menu interaction object with the associated delegate.

## Parameters

- `delegate`: The object that provides the contextual menu and responds to other interaction-related events. This object must adopt the   protocol.

## See Also

- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction/init(delegate:))*