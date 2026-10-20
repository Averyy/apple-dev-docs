# init(sidebarWithViewController:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a split view item that represents a sidebar for the specified view controller.

**Availability**:
- macOS 10.11+

## Declaration

```swift
convenience init(sidebarWithViewController viewController: NSViewController)
```

```objc
+ (instancetype) sidebarWithViewController:(NSViewController *) viewController;
```

#### Discussion

Sidebar items take advantage of the standard system appearance and behavior for sidebars, including:

- The translucent material background
- The ability to collapse and expand on split view size changes
- The ability to overlay at small split view sizes in full-screen mode

Additionally, sidebars use standard system default values for these properties:

- [`canCollapse`](./cancollapse.md) and [`isSpringLoaded`](./isspringloaded.md) are [`true`](../../Swift/true.md)
- [`minimumThickness`](./minimumthickness.md) and [`maximumThickness`](./maximumthickness.md) use the standard minimum and maximum sidebar size
- [`preferredThicknessFraction`](./preferredthicknessfraction.md) uses the standard fraction for sidebars (`0.15`)

## See Also

### Creating a split view item
- [convenience init(contentListWithViewController: NSViewController)](./init%28contentlistwithviewcontroller%29.md)
  Creates a split view item that represents a content list for the specified view controller.
- [convenience init(viewController: NSViewController)](./init%28viewcontroller%29.md)
  Creates a split view item that represents the specified view controller.
- [convenience init(inspectorWithViewController: NSViewController)](./init%28inspectorwithviewcontroller%29.md)
  Creates a split view item that represents an inspector for the specified view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/init(sidebarwithviewcontroller:))*