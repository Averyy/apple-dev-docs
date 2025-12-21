# init(sidebarWithViewController:)

**Framework**: AppKit  
**Kind**: init

Creates a split view item that represents a sidebar for the specified view controller.

**Availability**:
- macOS 10.11+

## Declaration

```swift
convenience init(sidebarWithViewController viewController: NSViewController)
```

#### Discussion

Sidebar items take advantage of the standard system appearance and behavior for sidebars, including:

- The translucent material background
- The ability to collapse and expand on split view size changes
- The ability to overlay at small split view sizes in full-screen mode

Additionally, sidebars use standard system default values for these properties:

- [`canCollapse`](nssplitviewitem/cancollapse.md) and [`isSpringLoaded`](nssplitviewitem/isspringloaded.md) are [`true`](https://developer.apple.com/documentation/Swift/true)
- [`minimumThickness`](nssplitviewitem/minimumthickness.md) and [`maximumThickness`](nssplitviewitem/maximumthickness.md) use the standard minimum and maximum sidebar size
- [`preferredThicknessFraction`](nssplitviewitem/preferredthicknessfraction.md) uses the standard fraction for sidebars (`0.15`)

## See Also

- [convenience init(contentListWithViewController: NSViewController)](nssplitviewitem/init(contentlistwithviewcontroller:).md)
  Creates a split view item that represents a content list for the specified view controller.
- [convenience init(viewController: NSViewController)](nssplitviewitem/init(viewcontroller:).md)
  Creates a split view item that represents the specified view controller.
- [convenience init(inspectorWithViewController: NSViewController)](nssplitviewitem/init(inspectorwithviewcontroller:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/init(sidebarwithviewcontroller:))*