# init(inspectorWithViewController:)

**Framework**: AppKit  
**Kind**: init

Creates a split view item that represents an inspector for the specified view controller.

**Availability**:
- macOS 11.0+

## Declaration

```swift
convenience init(inspectorWithViewController viewController: NSViewController)
```

#### Discussion

In macOS 14.0 and later, inspectors use standard system default values for these properties:

- [`canCollapse`](nssplitviewitem/cancollapse.md) is [`true`](https://developer.apple.com/documentation/swift/true).
- [`minimumThickness`](nssplitviewitem/minimumthickness.md) and [`maximumThickness`](nssplitviewitem/maximumthickness.md)are the standard inspector size (270) and aren’t resizable by default.

## See Also

- [convenience init(sidebarWithViewController: NSViewController)](nssplitviewitem/init(sidebarwithviewcontroller:).md)
  Creates a split view item that represents a sidebar for the specified view controller.
- [convenience init(contentListWithViewController: NSViewController)](nssplitviewitem/init(contentlistwithviewcontroller:).md)
  Creates a split view item that represents a content list for the specified view controller.
- [convenience init(viewController: NSViewController)](nssplitviewitem/init(viewcontroller:).md)
  Creates a split view item that represents the specified view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/init(inspectorwithviewcontroller:))*