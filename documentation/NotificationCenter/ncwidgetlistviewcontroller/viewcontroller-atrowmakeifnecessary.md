# viewController(atRow:makeIfNecessary:)

**Framework**: Notification Center  
**Kind**: method

Returns the content view controller associated with the specified row, or a new content view controller if desired.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func viewController(atRow row: Int, makeIfNecessary makeIfNecesary: Bool) -> NSViewController
```

#### Return Value

The content view controller associated with the specified row, if one exists. Returns `nil` if the row doesn’t have a content view controller and you don’t want to create one.

## Parameters

- `row`: The row in the list.
- `makeIfNecesary`: Specify   to create a new content view controller if none exists or   to reuse an existing row.

## See Also

- [var contents: [Any]](ncwidgetlistviewcontroller/contents.md)
  An array of objects to display in the list view.
- [func row(for: NSViewController) -> Int](ncwidgetlistviewcontroller/row(for:).md)
  Returns the row represented by the specified content view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/viewcontroller(atrow:makeifnecessary:))*