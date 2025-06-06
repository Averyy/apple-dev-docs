# row(for:)

**Framework**: Notification Center  
**Kind**: method

Returns the row represented by the specified content view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func row(for viewController: NSViewController) -> Int
```

#### Return Value

The row represented by the content view controller.

## Parameters

- `viewController`: The content view controller created by the delegate to display the object in the row.

## See Also

- [var contents: [Any]](ncwidgetlistviewcontroller/contents.md)
  An array of objects to display in the list view.
- [func viewController(atRow: Int, makeIfNecessary: Bool) -> NSViewController](ncwidgetlistviewcontroller/viewcontroller(atrow:makeifnecessary:).md)
  Returns the content view controller associated with the specified row, or a new content view controller if desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/row(for:))*