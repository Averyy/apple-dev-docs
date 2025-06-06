# init(contentListWithViewController:)

**Framework**: AppKit  
**Kind**: init

Creates a split view item that represents a content list for the specified view controller.

**Availability**:
- macOS 10.11+

## Declaration

```swift
convenience init(contentListWithViewController viewController: NSViewController)
```

#### Discussion

You use a content list to display information like the Mail app’s list of messages or the Notes app’s list of notes.

Content lists use standard system default values for these properties:

- [`minimumThickness`](nssplitviewitem/minimumthickness.md), [`maximumThickness`](nssplitviewitem/maximumthickness.md), and [`automaticMaximumThickness`](nssplitviewitem/automaticmaximumthickness.md) use the standard system defaults for content lists
- [`preferredThicknessFraction`](nssplitviewitem/preferredthicknessfraction.md) uses the standard fraction for content lists (`0.28` if an adjacent sidebar is visible, `0.33` if not)

## See Also

- [convenience init(sidebarWithViewController: NSViewController)](nssplitviewitem/init(sidebarwithviewcontroller:).md)
  Creates a split view item that represents a sidebar for the specified view controller.
- [convenience init(viewController: NSViewController)](nssplitviewitem/init(viewcontroller:).md)
  Creates a split view item that represents the specified view controller.
- [convenience init(inspectorWithViewController: NSViewController)](nssplitviewitem/init(inspectorwithviewcontroller:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/init(contentlistwithviewcontroller:))*