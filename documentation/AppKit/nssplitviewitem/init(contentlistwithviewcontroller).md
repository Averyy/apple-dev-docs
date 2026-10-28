# init(contentListWithViewController:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a split view item that represents a content list for the specified view controller.

**Availability**:
- macOS 10.11+

## Declaration

```swift
convenience init(contentListWithViewController viewController: NSViewController)
```

```objc
+ (instancetype) contentListWithViewController:(NSViewController *) viewController;
```

## Discussion

You use a content list to display information like the Mail app’s list of messages or the Notes app’s list of notes.

Content lists use standard system default values for these properties:

- [`minimumThickness`](./minimumthickness.md), [`maximumThickness`](./maximumthickness.md), and [`automaticMaximumThickness`](./automaticmaximumthickness.md) use the standard system defaults for content lists
- [`preferredThicknessFraction`](./preferredthicknessfraction.md) uses the standard fraction for content lists (`0.28` if an adjacent sidebar is visible, `0.33` if not)

## See Also

### Creating a split view item
- [convenience init(sidebarWithViewController: NSViewController)](./init%28sidebarwithviewcontroller%29.md)
  Creates a split view item that represents a sidebar for the specified view controller.
- [convenience init(viewController: NSViewController)](./init%28viewcontroller%29.md)
  Creates a split view item that represents the specified view controller.
- [convenience init(inspectorWithViewController: NSViewController)](./init%28inspectorwithviewcontroller%29.md)
  Creates a split view item that represents an inspector for the specified view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/init(contentlistwithviewcontroller:))*