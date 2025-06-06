# action

**Framework**: AppKit  
**Kind**: property

The action method to call when someone clicks on the toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var action: Selector? { get set }
```

#### Discussion

If you assign a custom view to the toolbar item, modifying this property updates the `action` property of the view or calls the `setAction:` method, if one of them exists. If the item doesn’t contain a custom view, the toolbar item manages the action directly.

## See Also

- [var target: AnyObject?](nstoolbaritem/target.md)
  The object that defines the action method the toolbar item calls when clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/action)*