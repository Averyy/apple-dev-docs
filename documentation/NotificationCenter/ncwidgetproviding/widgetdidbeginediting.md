# widgetDidBeginEditing()

**Framework**: Notification Center  
**Kind**: method

Called when a user chooses the widget’s begin editing button.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func widgetDidBeginEditing()
```

#### Discussion

This method can be called when [`widgetAllowsEditing`](ncwidgetproviding/widgetallowsediting.md) is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var widgetAllowsEditing: Bool](ncwidgetproviding/widgetallowsediting.md)
  A Boolean value indicating whether the widget can be edited by users.
- [func widgetDidEndEditing()](ncwidgetproviding/widgetdidendediting.md)
  Called when a widget’s editing session ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/widgetdidbeginediting())*