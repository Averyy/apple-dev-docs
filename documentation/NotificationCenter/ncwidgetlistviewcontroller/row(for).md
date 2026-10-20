# row(for:)

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method

Returns the row represented by the specified content view controller.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
func row(for viewController: NSViewController) -> Int
```

```objc
- (NSUInteger) rowForViewController:(NSViewController *) viewController;
```

#### Return Value

The row represented by the content view controller.

## Parameters

- `viewController`: The content view controller created by the delegate to display the object in the row.

## See Also

### Accessing Content
- [var contents: [Any]](./contents.md)
  An array of objects to display in the list view.
- [func viewController(atRow: Int, makeIfNecessary: Bool) -> NSViewController](./viewcontroller%28atrow,makeifnecessary%29.md)
  Returns the content view controller associated with the specified row, or a new content view controller if desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/row(for:))*