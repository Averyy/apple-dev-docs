# setActions(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the actions to display for different alert styles.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func setActions(_ actions: [UIUserNotificationAction]?, for context: UIUserNotificationActionContext)
```

#### Discussion

Use this method to set or change the actions associated with a specific context.

## Parameters

- `actions`: An array of   objects representing the actions to display for the given context. When displaying the notification to the user, the system displays the action buttons using the same order as the items in this array. If you specify   or an empty array, this method removes the actions for the specified context.
- `context`: The context in which the alert is displayed. For a list of possible values, see  .

## See Also

- [var identifier: String?](uimutableusernotificationcategory/identifier.md)
  The name of the action group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/setactions(_:for:))*