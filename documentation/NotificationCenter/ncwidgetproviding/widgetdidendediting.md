# widgetDidEndEditing()

**Framework**: Notification Center  
**Kind**: method

Called when a widget’s editing session ends.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func widgetDidEndEditing()
```

#### Discussion

This method is called when a user chooses the widget’s end editing button or when editing is deactivated because editing begins in a different widget. This method can be called when [`widgetAllowsEditing`](ncwidgetproviding/widgetallowsediting.md) is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var widgetAllowsEditing: Bool](ncwidgetproviding/widgetallowsediting.md)
  A Boolean value indicating whether the widget can be edited by users.
- [func widgetDidBeginEditing()](ncwidgetproviding/widgetdidbeginediting.md)
  Called when a user chooses the widget’s begin editing button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetdidendediting())*