# init(image:pullDownMenu:)

**Framework**: AppKit  
**Kind**: init

Creates a standard pull-down button with a title, optional image, and menu.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@backDeployed(before: macOS 15.0)
@MainActor @preconcurrency convenience init(image: NSImage, pullDownMenu: NSMenu)
```

#### Return Value

An initialized pull-down button object.

#### Discussion

Pull-down buttons created using this method have the `usesItemFromMenu` property set to `false`.

## Parameters

- `image`: The icon that is displayed on the button.
- `pullDownMenu`: The pull-down menu to present when interacting with the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/init(image:pulldownmenu:))*