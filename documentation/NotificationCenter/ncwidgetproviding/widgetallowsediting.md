# widgetAllowsEditing

**Framework**: Notification Center  
**Kind**: property

A Boolean value indicating whether the widget can be edited by users.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional var widgetAllowsEditing: Bool { get }
```

#### Discussion

When a widget that supports editing sets this property to [`true`](https://developer.apple.com/documentation/swift/true), it automatically gets a system-provided button in its header area that users choose to begin or end editing. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func widgetDidBeginEditing()](ncwidgetproviding/widgetdidbeginediting.md)
  Called when a user chooses the widget’s begin editing button.
- [func widgetDidEndEditing()](ncwidgetproviding/widgetdidendediting.md)
  Called when a widget’s editing session ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetallowsediting)*