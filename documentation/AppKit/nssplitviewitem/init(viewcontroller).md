# init(viewController:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a split view item that represents the specified view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
convenience init(viewController: NSViewController)
```

```objc
+ (instancetype) splitViewItemWithViewController:(NSViewController *) viewController;
```

## See Also

### Creating a split view item
- [convenience init(sidebarWithViewController: NSViewController)](./init%28sidebarwithviewcontroller%29.md)
  Creates a split view item that represents a sidebar for the specified view controller.
- [convenience init(contentListWithViewController: NSViewController)](./init%28contentlistwithviewcontroller%29.md)
  Creates a split view item that represents a content list for the specified view controller.
- [convenience init(inspectorWithViewController: NSViewController)](./init%28inspectorwithviewcontroller%29.md)
  Creates a split view item that represents an inspector for the specified view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewitem/init(viewcontroller:))*