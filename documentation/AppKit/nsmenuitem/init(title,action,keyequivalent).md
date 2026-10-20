# init(title:action:keyEquivalent:)

**Framework**: AppKit  
**Kind**: init

Returns an initialized instance of `NSMenuItem`.

**Availability**:
- macOS ?+

## Declaration

```swift
init(title string: String, action selector: Selector?, keyEquivalent charCode: String)
```

#### Return Value

An instance of `NSMenuItem`.

#### Discussion

For instances of the `NSMenuItem` class, the default initial state is `NSOffState`, the default on-state image is a check mark, and the default mixed-state image is a dash.

## Parameters

- `string`: The title of the menu item. This value must not be `nil` (if there is no title, specify an empty `NSString`).
- `selector`: The action selector to be associated with the menu item. This value must be a valid selector or `NULL`.
- `charCode`: A string representing a keyboard key to be used as the key equivalent. This value must not be `nil` (if there is no key equivalent, specify an empty `NSString`).

## See Also

- [class NSMenuItem](nsmenuitem.md)
  A command item in an app menu.
- [init(coder: NSCoder)](nsmenuitem/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/init(title:action:keyequivalent:))*