# init(title:action:keyEquivalent:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns an initialized instance of `NSMenuItem`.

**Availability**:
- macOS

## Declaration

```swift
init(title string: String, action selector: Selector?, keyEquivalent charCode: String)
```

```objc
- (instancetype) initWithTitle:(NSString *) string action:(SEL) selector keyEquivalent:(NSString *) charCode;
```

## Return Value

An instance of `NSMenuItem`.

## Discussion

For instances of the `NSMenuItem` class, the default initial state is `NSOffState`, the default on-state image is a check mark, and the default mixed-state image is a dash.

## Parameters

- `string`: The title of the menu item. This value must not be `nil` (if there is no title, specify an empty `NSString`).
- `selector`: The action selector to be associated with the menu item. This value must be a valid selector or `NULL`.
- `charCode`: A string representing a keyboard key to be used as the key equivalent. This value must not be `nil` (if there is no key equivalent, specify an empty `NSString`).

## See Also

### Related Documentation
- [class NSMenuItem](../nsmenuitem.md)
  A command item in an app menu.
### Creating a menu item
- [init(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/init(title:action:keyequivalent:))*