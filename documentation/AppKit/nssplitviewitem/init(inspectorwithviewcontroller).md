# init(inspectorWithViewController:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a split view item that represents an inspector for the specified view controller.

**Availability**:
- macOS 11.0+

## Declaration

```swift
convenience init(inspectorWithViewController viewController: NSViewController)
```

```objc
+ (instancetype) inspectorWithViewController:(NSViewController *) viewController;
```

#### Discussion

In macOS 14.0 and later, inspectors use standard system default values for these properties:

- [`canCollapse`](./cancollapse.md) is [`true`](../../Swift/true.md).
- [`minimumThickness`](./minimumthickness.md) and [`maximumThickness`](./maximumthickness.md)are the standard inspector size (270) and aren’t resizable by default.

## See Also

### Creating a split view item
- [convenience init(sidebarWithViewController: NSViewController)](./init%28sidebarwithviewcontroller%29.md)
  Creates a split view item that represents a sidebar for the specified view controller.
- [convenience init(contentListWithViewController: NSViewController)](./init%28contentlistwithviewcontroller%29.md)
  Creates a split view item that represents a content list for the specified view controller.
- [convenience init(viewController: NSViewController)](./init%28viewcontroller%29.md)
  Creates a split view item that represents the specified view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/init(inspectorwithviewcontroller:))*